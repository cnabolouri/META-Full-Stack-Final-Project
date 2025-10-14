from rest_framework import serializers
from restaurant.models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "price", "description"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id","first_name","last_name","guest_number","comment",
            "reservation_date","reservation_time"
        ]
        # user comes from request, not client

    def create(self, validated_data):
        return Booking.objects.create(user=self.context["request"].user, **validated_data)
