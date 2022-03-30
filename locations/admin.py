from django.contrib import admin
from .models import Location


# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """ display contact messages in admin """
    list_display = ('location', 'start_date', 'end_date')
