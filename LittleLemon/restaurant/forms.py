# from django import forms
# from django.forms import ModelForm
# from django.core.exceptions import ValidationError
# from .models import Booking

# class BookingForm(ModelForm):
#     class Meta:
#         model  = Booking
#         fields = "__all__"
#         widgets = {
#             "reservation_date": forms.DateInput(attrs={"type": "date"}),
#             # reservation_time renders as <select> because it has choices
#         }

#     def clean(self):
#         cleaned = super().clean()
#         d = cleaned.get("reservation_date")
#         t = cleaned.get("reservation_time")
#         if d and t and Booking.objects.filter(reservation_date=d, reservation_time=t).exists():
#             raise ValidationError("That time slot is already booked for the selected date.")
#         return cleaned


from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "first_name", "last_name", "guest_number",
            "reservation_date", "reservation_time", "comment"
        ]
