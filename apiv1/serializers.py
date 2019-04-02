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

    tour_group = TourGroupSerializer()

    class Meta:
        model = Tour

        fields = ['pk', 'tour_group', 'start', 'end', 'price']


class TourRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourRegistration
        fields = ['pk', 'tour', 'title','profile', 'group', 'quantity', 'is_persian']
        

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['pk', 'tour_registration', 'first_name', 'email', 'phone', 'passport_number',
        'last_name', 'national_id', 'nationality', 'city', 'birth_date','description', 'is_persian']
