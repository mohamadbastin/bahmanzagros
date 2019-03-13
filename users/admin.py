from django.contrib import admin

# Register your models here.
from users.models import UserProfile
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(UserProfile)
