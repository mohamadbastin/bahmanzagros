from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from tour.models import *
from users.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status
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
            return None

class TourGroupVarientList(GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        tgp_id = kwargs['tour_id']
        try:
            tgp = TourGroup.objects.get(pk=tgp_id)
            tgp_data = TourGroupSerializer(instance=tgp).data
            tgp_data['image'] = "http://" + request.META['HTTP_HOST'] + tgp_data['image']

            variants = Tour.objects.filter(tour_group=tgp)
            variants_data = TourSerializer(variants, many=True).data

            return Response({"tour_group": tgp_data, "variants": variants_data})
        except:
            return Response({"Error": "No data"}, status=status.HTTP_404_NOT_FOUND)


class TourVariantRegistrationList(GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        v_id = kwargs['variant_id']
        try:
            profile = request.user.user_profile
            v = Tour.objects.get(pk=v_id)
            v_data = TourSerializer(instance=v).data

            registrations = TourRegistration.objects.filter(tour=v,profile=profile)
            registrations_data = TourRegistrationSerializer(registrations, many=True).data

            return Response({"variant": v_data, "registrations": registrations_data})
        except:
            return Response({"Error": "No data"}, status=status.HTTP_404_NOT_FOUND)

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
