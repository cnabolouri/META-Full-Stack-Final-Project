from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Optional: allow clients to control page size with ?page_size=
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50

# MENU
class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by("id")
    serializer_class = MenuSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]  # adjust if you want auth
    # enable search by name and order by price via settings' backends
    search_fields = ["name", "description"]
    ordering_fields = ["price", "name"]          # ?ordering=price or -price

class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

# BOOKINGS
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by("-id")
    serializer_class = BookingSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]
    search_fields = ["first_name", "last_name", "comment"]
    ordering_fields = ["id", "first_name", "last_name"]

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]
