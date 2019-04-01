from django.contrib import admin

# Register your models here.
from users.models import UserProfile
from django.contrib.auth.models import User, Group


<<<<<<< HEAD
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'email', 'phone_number', 'info']


# admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(UserProfile, UserProfileAdmin)
=======
admin.site.register(UserProfile)
>>>>>>> 2067a9ff52af1e1f630706d9f0bb3c323bca6988
