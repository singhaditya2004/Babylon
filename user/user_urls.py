from django.urls import path
from . import views 
from .views import (
    home_view,
    services_view,
    contact_view,
    signup_view,
    login_view,
    logout_view,
    book_slot,
    slot_availability
)

urlpatterns = [
    path('', home_view, name='home'),
    path('services/', services_view, name='services'),
    path('contact/', contact_view, name='contact'),

   path('login/', login_view, name='login'),
   path('signup/', signup_view, name='signup'),
   path('logout/', logout_view, name='logout'),
   path('book/', book_slot, name='book_slot'),
   path("slots/", slot_availability, name="slot_availability"),


]
