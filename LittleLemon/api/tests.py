from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Menu, Booking

class ApiSmoke(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="anna", password="pass1234")
        self.menu = Menu.objects.create(name="Bruschetta", price=8, description="Toasted bread")

    def test_menu_list(self):
        res = self.client.get("/api/menu/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data["results"]) >= 1)

    def test_booking_requires_auth(self):
        payload = {
            "first_name":"A","last_name":"B","guest_number":2,"comment":"",
            "reservation_date": "2025-10-20","reservation_time":"18:00"
        }
        res = self.client.post("/api/bookings/", payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_booking_create_and_list_own(self):
        self.client.login(username="anna", password="pass1234")
        payload = {
            "first_name":"A","last_name":"B","guest_number":2,"comment":"",
            "reservation_date": "2025-10-20","reservation_time":"18:00"
        }
        res = self.client.post("/api/bookings/", payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res2 = self.client.get("/api/bookings/?date=2025-10-20")
        self.assertEqual(res2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res2.data["results"]), 1)
