from rest_framework import serializers
from tour.models import *
from django.contrib.auth.models import User
from users.models import UserProfile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'email', 'phone_number', 'info']

class TourGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGroup

        fields = ['pk', 'title', 'description', 'image']


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour

        fields = ['pk', 'tour_group', 'start', 'end', 'price']


class TourRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourRegistration

        fields = ['pk', 'tour', 'profile', 'group', 'quantity', 'date_registered']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['pk', 'tour_registration', 'name', 'email', 'phone', 'passport_number']
