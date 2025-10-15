"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView
# from django.contrib.auth.views import LogoutView


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('bookings', r_views.BookingListCreate.as_view(), name="booking-list-create"),
#     path('', include('restaurant.urls')),
#     path("", TemplateView.as_view(template_name="index.html"), name="home"),
#     path("api/", include("api.urls")),
#     path("auth/", include("djoser.urls")),
#     path("accounts/logout/", LogoutView.as_view(next_page="home"), name="logout"),
#     path("auth/", include("djoser.urls.authtoken")),  # /auth/token/login/, /auth/token/logout/

# ]


# littlelemon/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),

    # your site/app urls
    path("", include(("restaurant.urls", "restaurant"), namespace="restaurant")),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),

    # API
    path("api/", include("api.urls")),

    # Browser (session) auth
    path("accounts/", include("django.contrib.auth.urls")),  # /accounts/login, /logout, etc.
    path(
        "accounts/logout/",
        LogoutView.as_view(next_page="home"),
        name="logout",
    ),

    # Djoser token endpoints for API clients only (Insomnia / mobile apps)
    path("auth/", include("djoser.urls")),                  # optional user endpoints
    path("auth/", include("djoser.urls.authtoken")),        # /auth/token/login, /auth/token/logout
]
