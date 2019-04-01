from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("tour-groups", TourGroupViewSet)
router.register("tour", TourViewSet)
router.register("tour-registrations", TourRegistrationViewSet)
router.register("ticket", TicketViewSet)
# router.register("profiletour", ProfileTourViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("profiletour", ProfileTourViewSet.as_view()),
    path("profileticket", ProfileTicketViewSet.as_view())
]

