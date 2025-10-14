# from django.db import models
from django.contrib.auth.models import User

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
#     first_name = models.CharField(max_length=200)
#     last_name  = models.CharField(max_length=200)
#     guest_number = models.IntegerField()
#     comment = models.CharField(max_length=1000, blank=True)
#     reservation_date = models.DateField()
#     reservation_time = models.TimeField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"



from django.db import models
from django.conf import settings
from datetime import time

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
   
    first_name       = models.CharField(max_length=200)
    last_name        = models.CharField(max_length=200)
    guest_number     = models.IntegerField()
    comment          = models.CharField(max_length=1000)

    reservation_date = models.DateField(null=True, blank=True)

    TIME_SLOTS = [(time(h, 0), f"{(h-1)%12+1} {'AM' if h < 12 else 'PM'}")
                  for h in range(10, 21)]
    reservation_time = models.TimeField(choices=TIME_SLOTS, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["reservation_date", "reservation_time"],
                name="unique_reservation_slot"
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
