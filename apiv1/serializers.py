from rest_framework import serializers
from tour.models import *


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


# class TicketListSerializer(serializers.Serializer):
#     class Meta:
#         fields = ['TicketList']
#
#     def create(self, validated_data):
#
#         for i in self.context["TicketList"]:
#             tmp = Ticket(tour_registration=TourRegistration.objects.filter(id=i["tour_registration"]).first(),
#                          name=i["name"],
#                          email=i["email"],
#                          phone=i["phone"],
#                          passport_number=i["passport_number"])
#             tmp.save()
#         super(TicketListSerializer, self).create(validated_data)
#         return tmp

# class TicketListSerializer(serializers.Serializer):
#     class Meta:
#         fields = ['TicketList']
#
#     def create(self, validated_data):
#         print("boz")
#         return Ticket(**validated_data)
#
#     def update(self, instance, validated_data):
#         print(self.context["TicketList"])
#         for i in self.context["TicketList"]:
#             tmp = Ticket(tour_registration=TourRegistration.objects.filter(id=i["tour_registration"]).first(),
#                          name=i["name"],
#                          email=i["email"],
#                          phone=i["phone"],
#                          passport_number=i["passport_number"])
#             tmp.save()
#             return super(TicketListSerializer, self).update(instance, validated_data)
