from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .forms import BookingForm
from .models import Booking, Menu

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.dateparse import parse_date
from datetime import datetime

from rest_framework import viewsets, permissions, filters
from .serializers import MenuSerializer, BookingSerializer


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def book(request):
    submitted = False
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Avoid double submit on refresh
            return redirect("/book/?submitted=True")
    else:
        form = BookingForm()
        if "submitted" in request.GET:
            submitted = True

    return render(request, "book.html", {"form": form, "submitted": submitted})

def menu(request):
    menu_data = Menu.objects.all().order_by("name")   # alphabetical for peer review
    main_data = {"menu": menu_data}
    return render(request, "menu.html", main_data)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = get_object_or_404(Menu, pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


def account(request):
    # Render one page for both states; template toggles on user.is_authenticated
    return render(request, "account.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("book")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Prevent double-booking for the same slot (any user)
            cd = form.cleaned_data
            exists = Booking.objects.filter(
                reservation_date=cd["reservation_date"],
                reservation_time=cd["reservation_time"]
            ).exists()
            if exists:
                form.add_error("reservation_time", "This time is already booked.")
            else:
                booking = form.save(commit=False)
                booking.user = request.user  # lock to current user
                booking.save()
                return redirect("reservations")
    else:
        form = BookingForm()
    return render(request, "book.html", {"form": form})

def bookings_api(request):
    """
    Public endpoint used by the Book page’s JS to disable taken time slots.
    It returns only the list of reserved times for a given date (no names/emails).
    Example: GET /bookings?date=2025-10-12 -> {"date":"2025-10-12","reserved":["10:00","11:30"]}
    """
    date_str = request.GET.get("date")
    if not date_str:
        return HttpResponseBadRequest("Missing ?date=YYYY-MM-DD")

    date_obj = parse_date(date_str)
    if not date_obj:
        return HttpResponseBadRequest("Invalid date")

    qs = Booking.objects.filter(reservation_date=date_obj).values_list("reservation_time", flat=True)
    reserved_times = sorted({t.strftime("%H:%M") for t in qs})
    return JsonResponse({"date": date_str, "reserved": reserved_times})

@login_required
def reservations(request):
    # Only THIS user’s bookings, rendered nicely (not JSON)
    my = (Booking.objects
          .filter(user=request.user)
          .order_by("-reservation_date", "-reservation_time", "-id"))
    return render(request, "reservations.html", {"bookings": my})


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, "user_id", None) == request.user.id

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by("id")
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["price", "name"]
    search_fields = ["name", "description"]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        qs = Booking.objects.filter(user=self.request.user).order_by("-reservation_date","-reservation_time")
        date = self.request.query_params.get("date")
        if date:
            qs = qs.filter(reservation_date=date)
        return qs