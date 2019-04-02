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
    tour_group = models.ForeignKey(TourGroup, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tour_group.title) + ' ' + str(self.start) + ' TO' + str(self.end)


class TourRegistration(models.Model):
    title = models.CharField(max_length=255)
    tour = models.ForeignKey(Tour, related_name="tour_registrations", on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    group = models.BooleanField()
    quantity = models.IntegerField()
    date_registered = models.DateTimeField(auto_now_add=True)
    
    is_persian = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.tour) + " " + str(self.profile)


class Ticket(models.Model):
    tour_registration = models.ForeignKey(TourRegistration, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    national_id = models.CharField(max_length=20, blank=True, null=True)
    passport_number = models.BigIntegerField(blank=True, null=True)

    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    
    nationality = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    description= models.TextField(max_length=500, blank=True, null=True)
    
    is_persian = models.BooleanField(default=True)

    def __str__(self):
        return str(self.tour_registration)
