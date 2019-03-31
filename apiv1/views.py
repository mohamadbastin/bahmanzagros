from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from tour.models import *
from users.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

# Create your views here.

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

    def create(self, request, *args, **kwargs):
        # do your thing here
        data = request.data
        for i in data["ticket"]:
            tmp = Ticket(tour_registration=TourRegistration.objects.filter(id=i["tour_registration"]).first(), name=i["name"],
                         email=i["email"],
                         phone=i["phone"],
                         passport_number=i["passport_number"])
            tmp.save()

        return super().create(request)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
