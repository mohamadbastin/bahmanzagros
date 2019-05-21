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

        fields = ['pk', 'is_daily', 'title', 'tour_group', 'start', 'description', 'end', 'price']


class TourRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourRegistration
        fields = ['pk', 'tour', 'title', 'date', 'group', 'count', 'quantity', 'is_persian']

    def create(self, validated_data):
        validated_data.pop('data')
        ct = validated_data.pop('context')
        new_tr = TourRegistration(**validated_data)
        new_tr.profile = ct['profile']
        new_tr.save()
        return new_tr


class TourRegistrationSerializerGet(serializers.ModelSerializer):
    tour = TourSerializer()

    class Meta:
        model = TourRegistration
        fields = ['pk', 'tour', 'title', 'date', 'profile', 'group', 'count', 'quantity', 'is_persian']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['pk', 'tour_registration', 'first_name', 'email', 'phone', 'address', 'passport_number',
                  'last_name', 'national_id', 'nationality', 'city', 'address', 'birth_date', 'description',
                  'is_persian']
