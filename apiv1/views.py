from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializers import *
from tour.models import *
from users.models import UserProfile


# Create your views here.


class TourGroupViewSet(viewsets.ModelViewSet):
    queryset = TourGroup.objects.all()
    serializer_class = TourGroupSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.filter(visible=True)
    serializer_class = TourSerializer


class TourRegistrationViewSet(viewsets.ModelViewSet):
    queryset = TourRegistration.objects.all()
    serializer_class = TourRegistrationSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ProfileTourViewSet(ListAPIView):
    serializer_class = TourRegistrationSerializer

    def get_queryset(self):
        user = self.request.user
        return TourRegistration.objects.filter(profile=user.user_profile)


class ProfileTicketViewSet(ListAPIView):
    serializer_class = TicketSerializer()

    def get_queryset(self):
        user = self.request.user
        tour_registration = TourRegistration.objects.filter(profile=user.user_profile)
        tickets = []
        for i in tour_registration:
            tickets.append(i.ticket_tour)
            # print(i.ticket_tour)
        return tickets
