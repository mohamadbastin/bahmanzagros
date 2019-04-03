from django.contrib import admin

# Register your models here.
from users.models import UserProfile
from django.contrib.auth.models import User, Group


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'email', 'phone_number', 'info']


# admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(UserProfile)

