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
    title = models.CharField(max_length=50)
    description = models.TextField()
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    price = models.CharField(max_length=50)

    @property
    def is_daily(self):
        return self.start is None and self.end is None

    def __str__(self):
        if self.start is None and self.end is None:
            return str(self.tour_group.title) + ' ' + 'Daily Tour'
        else:
            return str(self.tour_group.title) + ' ' + str(self.start) + ' TO ' + str(self.end)

class TourRegistration(models.Model):
    title = models.CharField(max_length=255)
    tour = models.ForeignKey(Tour, related_name="tour_registrations", on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    group = models.BooleanField()
    count = models.IntegerField(blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    
    is_persian = models.BooleanField(default=True)
    
    @property
    def quantity(self):
        if self.group:
            return self.count
        return len(self.tickets.all())

    def __str__(self):
        return str(self.title)


class Ticket(models.Model):
    tour_registration = models.ForeignKey(TourRegistration, on_delete=models.CASCADE, related_name="tickets")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    national_id = models.CharField(max_length=20, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)

    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    nationality = models.CharField(max_length=30, blank=True, null=True, default="-")
    city = models.CharField(max_length=30, blank=True, null=True, default="-")

    birth_date = models.DateField(blank=True, null=True)
    description= models.TextField(max_length=500, blank=True, null=True)
    
    is_persian = models.BooleanField(default=True)

    def __str__(self):
        return str(self.tour_registration)
