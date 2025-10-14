from django.contrib import admin

# Register your models here.
from .models import Menu, Booking

admin.site.register(Menu)
admin.site.register(Booking)
# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ("name", "price")
#     search_fields = ("name",)
