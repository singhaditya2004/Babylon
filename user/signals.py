from django.contrib.auth.signals import user_logged_in  
from django.dispatch import receiver
from django.core.mail import mail_admins

@receiver(user_logged_in)
def admin_user_login(sender, request, user, **kwargs):
    subject = "User Login Alert"

    message = f"""
A user has logged in.

Username: {user.username}
Name: {user.first_name} {user.last_name}
Email: {user.email}

"""

    mail_admins(subject, message)
from django.db.models.signals import post_save
from .models import Booking

@receiver(post_save, sender=Booking)
def admin_booking_notification(sender, instance, created, **kwargs):
    if created:
        subject = "New Slot Booked"

        message = f"""
A new booking has been made.

User: {instance.user.username}
Name: {instance.user.first_name} {instance.user.last_name}
Email: {instance.user.email}
Date: {instance.date}
Time Slot: {instance.time_slot}
"""

        mail_admins(subject, message)

