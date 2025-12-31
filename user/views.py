from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking


def home_view(request):
    return render(request, 'Home.html')





def check_availability(date, time_slot):
    return not Booking.objects.filter(date=date, time_slot=time_slot).exists()



def services_view(request):
    return render(request, 'services.html')

def contact_view(request):
    return render(request, 'contact.html')

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        User.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password1']
        )
        return redirect('login')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def book_slot(request):
    if request.method == "POST":
        date = request.POST.get("date")
        time_slot = request.POST.get("time_slot")

        if Booking.objects.filter(date=date, time_slot=time_slot).exists():
            messages.error(request, "❌ Slot not available")
        else:
            Booking.objects.create(
                user=request.user,
                date=date,
                time_slot=time_slot
            )
            messages.success(request, "✅ Slot booked successfully")

    return render(request, "book.html")


def slot_availability(request):
    selected_date = request.GET.get("date")

    time_slots = [
        "10AM-11AM",
        "11AM-12PM",
        "12PM-1PM",
        "2PM-3PM",
    ]

    booked_slots = []

    if selected_date:
        booked_slots = Booking.objects.filter(
            date=selected_date
        ).values_list("time_slot", flat=True)

    context = {
        "time_slots": time_slots,
        "booked_slots": booked_slots,
        "selected_date": selected_date,
    }

    return render(request, "slot_availability.html", context)