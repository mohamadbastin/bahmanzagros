from django.db import models
# from rest_framework import serializers
from django.db.models.signals import post_save
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
    tour = models.ForeignKey(Tour, related_name="tour_registrations", on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    group = models.BooleanField()
    count = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField()
    price = models.CharField(max_length=100, blank=True, null=True)
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
def tour_reg_post_save(sender, instance, created, **kwargs):
    try:
        log = instance.log
    except Log.DoesNotExist:
        log = Log()

        log.profile = profile=instance.profile,
        log.tour_reg = tour_reg=instance,
        log.tour_title = tour_title=instance.tour.tour_group.title,
        log.count = instance.quantity
        log.is_persian = instance.is_persian
        log.price = instance.price
        log.status = instance.status
        log.verified_count = instance


class Log(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="log")
    tour_reg = models.OneToOneField(TourRegistration, on_delete=models.SET_NULL, null=True, blank=True, related_name="log")
    tour_title = models.CharField(max_length=255)
    added_date = models.DateField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    is_persian = models.BooleanField(default=True)
    price = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    verified_count = models.PositiveIntegerField(default=0)
    verified_price = models.CharField(max_length=255)


class Ticket(models.Model):
    tour_registration = models.ForeignKey(TourRegistration, on_delete=models.CASCADE, related_name="tickets")
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
def send_mail_verif(sender, instance, **kwargs):

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
