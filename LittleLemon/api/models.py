# from django.db import models
# from django.conf import settings
# from datetime import time
# # Create your models here.
# class Booking(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name  = models.CharField(max_length=200)
#     guest_number = models.IntegerField()
#     comment = models.CharField(max_length=1000, blank=True)
#     reservation_date = models.DateField()
#     reservation_time = models.TimeField()
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")

#     class Meta:
#         unique_together = ("user", "reservation_date", "reservation_time")  # prevent double booking per-user/slot

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} @ {self.reservation_date} {self.reservation_time}"


# class Menu(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.IntegerField()
#     description = models.TextField(max_length=1000, default='')

#     def __str__(self):
#         return self.name
