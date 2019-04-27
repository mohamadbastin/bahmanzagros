from rest_framework.authtoken.models import Token
from django.contrib import admin

admin.site.unregister(Token)
