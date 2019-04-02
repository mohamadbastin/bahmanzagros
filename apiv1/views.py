from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from tour.models import *
from users.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView

# Create your views here.


class GetTourRegistrationTikets(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = TicketSerializer

    def get_queryset(self):
        tr_id = self.kwargs['id']
        try:
            tr = TourRegistration.objects.get(pk=tr_id)
            return Ticket.objects.filter(tour_registration=tr)
        except:
            print("hrerer", tr_id)
            return None

class ProfileSerializer(RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProfileSerializer
    lookup_field = None
    def get_queryset(self):
        profile = self.request.user.user_profile
        return profile
    
    def get_object(self):
        return self.get_queryset()

class TourGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    
    queryset = TourGroup.objects.all()
    serializer_class = TourGroupSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourRegistrationViewSet(viewsets.ModelViewSet):
    queryset = TourRegistration.objects.all()
    serializer_class = TourRegistrationSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
