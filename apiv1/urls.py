from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("tour-groups", TourGroupViewSet)
router.register("tour", TourViewSet)
router.register("tour-registrations", TourRegistrationViewSet)
router.register("ticket", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("profile/detail/", ProfileSerializer.as_view()),
]

