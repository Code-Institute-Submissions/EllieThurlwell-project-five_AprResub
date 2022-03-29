from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ display contact messages in admin """
    list_display = ('name', 'email', 'message')
