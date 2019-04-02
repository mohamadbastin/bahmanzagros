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
    path("profile/detail/", ProfileSerializer.as_view()),
    path("tour-groups/<int:tour_id>/variants/", TourGroupVarientList.as_view()),
]

