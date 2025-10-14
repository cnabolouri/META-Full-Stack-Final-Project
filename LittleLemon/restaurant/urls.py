from django.urls import path
from . import views
from . import api
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path("book", web_views.booking_form, name="book"),
    # path("reservations", web_views.reservations_page, name="reservations"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:pk>/", views.display_menu_item, name="menu_item"),
    path("reservations/", views.reservations, name="reservations"),
    path("reservations/", views.reservations, name="reservations"),
    path("bookings", views.bookings_api, name="bookings_api"),

        # Auth
    path("account/", views.account, name="account"),
    path("accounts/login/",  auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.signup, name="signup"),

        # ---- API endpoints ----
    path("api/menu/", api.MenuListCreateView.as_view(), name="api_menu_list"),
    path("api/menu/<int:pk>/", api.MenuDetailView.as_view(), name="api_menu_detail"),
    path("api/bookings/", api.BookingListCreateView.as_view(), name="api_booking_list"),
    path("api/bookings/<int:pk>/", api.BookingDetailView.as_view(), name="api_booking_detail"),

]
