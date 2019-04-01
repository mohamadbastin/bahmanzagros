from django.db import models
from rest_framework import serializers
from users.models import UserProfile


# Create your models here.

class TourGroup(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    image = models.ImageField()

    # tour = models.ForeignKey(Tour)

    def __str__(self):
        return str(self.title)


class Tour(models.Model):
    visible = models.BooleanField()
    tour_group = models.ForeignKey(TourGroup, on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tour_group.title) + ' ' + str(self.start) + ' TO' + ' ' + str(self.end)


class TourRegistration(models.Model):
    tour = models.ForeignKey(Tour, related_name="tour_registrations", on_delete=models.PROTECT)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_group = models.BooleanField()
    quantity = models.IntegerField()
    is_local = models.BooleanField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.tour) + " " + str(self.profile)


class Ticket(models.Model):
    tour_registration = models.ForeignKey(TourRegistration, on_delete=models.PROTECT, related_name='ticket_tour')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    passport_number = models.BigIntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return str(self.tour_registration)
