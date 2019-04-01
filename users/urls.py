from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users'

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
