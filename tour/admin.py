from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token


class TicketAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'verified')
    list_display_links = ['first_name', ]
    list_editable = ('verified',)


class TourRegistrationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tour', 'profile', 'date', 'count', 'price', 'verified')
    list_display_links = ['tour',]
    list_filter = ['date', ]
    search_fields = ['date', ]
    list_editable = ('price', 'verified')


admin.site.register(TourRegistration, TourRegistrationAdmin)
admin.site.register(Tour)
admin.site.register(TourGroup)
admin.site.register(Ticket, TicketAdmin)
# admin.site.unregister(Token)
# Register your models here.
