from django.shortcuts import render
from rest_framework import viewsets

from tourmanagement import settings
from .serializers import *
from tour.models import *
from users.models import UserProfile
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import QueryDict
from django.utils import timezone

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

            now = timezone.now().date()

            tmpvariants = Tour.objects.filter(tour_group=tgp)

            variants = []

            for variant in tmpvariants:
                if not variant.end:
                    variants += [variant,]
                elif variant.end >= now:
                    variants += [variant,]


            variants_data = TourSerializer(variants, many=True).data

            return Response({"tour_group": tgp_data, "variants": variants_data})
        except:

            if settings.DEBUG:
                raise

            return Response({"Error": "No data"}, status=status.HTTP_404_NOT_FOUND)


class TourVariantRegistrationList(GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        v_id = kwargs['variant_id']
        try:
            profile = request.user.user_profile
            v = Tour.objects.get(pk=v_id)
            v_data = TourSerializer(instance=v).data

            registrations = TourRegistration.objects.filter(tour=v, profile=profile).order_by('-pk')
            registrations_data = TourRegistrationSerializer(registrations, many=True).data

            return Response({"variant": v_data, "registrations": registrations_data})
        except:
            return Response({"Error": "No data"}, status=status.HTTP_404_NOT_FOUND)


class TourRegistrationTicketsList(GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        tour_registration_id = kwargs['tour_reg_id']

        try:
            tour_registration = TourRegistration.objects.get(pk=tour_registration_id)
            tour_reg_data = TourRegistrationSerializerGet(tour_registration).data
            tickets = Ticket.objects.filter(tour_registration=tour_registration).order_by('-pk')
            tickets_data = TicketSerializer(tickets, many=True).data
            return Response({'tour': tour_reg_data,
                             'tickets': tickets_data})
        except TourRegistration.DoesNotExist:
            return Response({"Error": "Tour registration not found"}, status=status.HTTP_404_NOT_FOUND)


class TourRegistrationCreate(CreateAPIView):
    serializer_class = TourRegistrationSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(data=self.request.data, context={'profile': self.request.user.user_profile})

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     profile = request.user.user_profile

    # data = {}
    # data['title'] = request.data.title
    # data['tour'] = request.data.tour
    # data['group'] = request.data.group
    # data['date'] = request.data.date
    # data['is_persian'] = request.data.is_persian
    # data['count'] = request.data.count
    # data['profile'] = profile

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         return Response("goopd")
    #     else:
    #         return Response("Error")


class ProfileSerializer(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    lookup_field = None

    def get_queryset(self):
        profile = self.request.user.user_profile
        return profile

    def get_object(self):
        return self.get_queryset()


class TourGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]

    queryset = TourGroup.objects.all().order_by('-pk')
    serializer_class = TourGroupSerializer




class ProfileTourRegs(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = TourRegistrationSerializerGet

    def get_queryset(self):
        profile = self.request.user.user_profile
        return profile.tour_regs.all()


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourRegistrationViewSet(viewsets.ModelViewSet):
    queryset = TourRegistration.objects.all()
    serializer_class = TourRegistrationSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
