from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register("menu", MenuViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="bookings")

urlpatterns = router.urls