from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token
from rangefilter.filter import DateRangeFilter

class TicketAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','city', 'tour','date', 'nationality', 'phone', 'email', 'profile','verified')
    list_display_links = ['first_name', ]
    list_editable = ('verified',)




    def tour(self, instance):
        return instance.tour_registration.tour.title

    def date(self, instance):
        return instance.tour_registration.date

    def profile(self, instance):
        return instance.tour_registration.profile

    list_filter = ['tour_registration__tour__title', ('tour_registration__date', DateRangeFilter), 'tour_registration__profile__user__username']


class TourRegistrationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tour', 'tour_start', 'tour_end','profile', 'count', 'price', 'profile', 'verified')

    def tour_start(self, instance):
        return instance.tour.start

    def tour_end(self, instance):
        return instance.tour.end



    list_display_links = ['tour',]
    list_filter = [('date', DateRangeFilter), 'profile__user__username']
    list_editable = ('count', 'price', 'verified')

class TourAdmin(admin.ModelAdmin):
    list_filter = ['title', 'tour_group', 'start', 'end', 'price']

admin.site.register(TourRegistration, TourRegistrationAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(TourGroup)
admin.site.register(Ticket, TicketAdmin)
# admin.site.unregister(Token)
# Register your models here.
