from django.shortcuts import render

def booking_form(request):
    return render(request, "book.html")

def reservations_page(request):
    return render(request, "reservations.html")
