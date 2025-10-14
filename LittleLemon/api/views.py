from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters
from restaurant.models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

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
