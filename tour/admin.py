from django.contrib import admin
from .models import *
from rangefilter.filter import DateRangeFilter


class TicketAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city','tour_group','tour', 'date', 'nationality',
                    'phone', 'email', 'profile', 'verified')
    list_display_links = ['first_name', ]
    list_editable = ('verified', )

    def tour_group(self, instance):
        return instance.tour_registration.tour_group_title

    def tour(self, instance):
        return instance.tour_registration.title

    def date(self, instance):
        return instance.tour_registration.date

    def profile(self, instance):
        return instance.tour_registration.profile

    list_filter = ['tour_registration__tour__title', 'tour_registration__date',
                   'tour_registration__profile__user__username']


class TourRegistrationAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'tour_group_title', 'date', 'count', 'price', 'verified_price','verified_count', 'profile', 'verified')

    list_display_links = ['title', ]
    list_filter = [('date', DateRangeFilter), 'profile__user__username', 'verified']
    list_editable = ('verified_count', 'verified_price', 'verified')


class TourAdmin(admin.ModelAdmin):
    list_filter = ['title', 'tour_group', 'start', 'end', 'price']
    list_display = ['title', 'tour_group', 'start', 'end', 'price']


admin.site.register(TourRegistration, TourRegistrationAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(TourGroup)
admin.site.register(Ticket, TicketAdmin)