from django.db import models
# from rest_framework import serializers
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import UserProfile
from django_jalali.db import models as jmodels
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your models here.

class TourGroup(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    image = models.ImageField()

    # tour = models.ForeignKey(Tour)

    def __str__(self):
        return str(self.title)


class Tour(models.Model):
    tour_group = models.ForeignKey(TourGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    price = models.TextField()

    @property
    def tour_gp_name(self):
        return str(self.tour_group.title)

    @property
    def is_daily(self):
        return self.start is None and self.end is None

    def __str__(self):
        if self.start is None and self.end is None:
            return str(self.tour_group.title) + ' ' + 'Daily Tour'
        else:
            return str(self.tour_group.title)


class TourRegistration(models.Model):
    title = models.CharField(max_length=255)
    tour = models.ForeignKey(Tour, related_name="tour_registrations", on_delete=models.SET_NULL, blank=True, null=True)

    tour_group_title = models.CharField(max_length=255)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="tour_regs")
    group = models.BooleanField()
    date = models.DateField()
    count = models.PositiveIntegerField(blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)

    verified_count = models.PositiveIntegerField(blank=True, null=True)
    verified_price = models.CharField(max_length=100, blank=True, null=True)

    is_persian = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)

    @property
    def quantity(self):
        if self.group:
            return self.count
        return len(self.tickets.all())

    def __str__(self):
        return str(self.pk)


@receiver(post_save, sender=TourRegistration)
def add_tour_title(sender, instance, created, **kwargs):

    if created:
        instance.tour_group_title = instance.tour.tour_group.title
        instance.price = instance.tour.price

        instance.save()


class Ticket(models.Model):
    tour_registration = models.ForeignKey(TourRegistration, on_delete=models.CASCADE, blank=True,null=True, related_name="tickets")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    national_id = models.CharField(max_length=20, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)

    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)

    nationality = models.CharField(max_length=30, blank=True, null=True, default="-")
    city = models.CharField(max_length=30, blank=True, null=True, default="-")

    birth_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    is_persian = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tour_registration)


@receiver(post_save, sender=Ticket, dispatch_uid="send_mail")
def send_mail_verif(sender, instance, created, **kwargs):

    msg_html = render_to_string('templates/tour/ticket_mail.html', {'ticket': instance})
    msg_plain = render_to_string('tour/ticket_mail.html', {'ticket': instance})

    send_mail(
        subject='Bahman Tours | Ticket Verification',
        message=msg_plain,
        html_message=msg_html,
        from_email='bahmanmardanloo27@gmail.com',
        recipient_list=[instance.email],
        fail_silently=False,
    )
