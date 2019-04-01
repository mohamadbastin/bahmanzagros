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
<<<<<<< HEAD
    path("profiletour", ProfileTourViewSet.as_view()),
    path("profileticket", ProfileTicketViewSet.as_view())
=======
    path("profile/detail/", ProfileSerializer.as_view()),
>>>>>>> 2067a9ff52af1e1f630706d9f0bb3c323bca6988
]

