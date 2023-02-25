from django.contrib import admin
from .models import Calendar, Event, Invitees
from .models import CustomUser

from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'is_staff',]
    list_display_links = ['username', ]
    fieldsets = UserAdmin.fieldsets + (
    (None,
        {
            'fields': ("name",)
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
    (None, 
        {
            'fields': ("name",)
            }
        ),
    )

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'owner',]
    list_display_links = ['id', 'name',]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'location', 'owner', 'start', 'end']
    list_display_links = ['id', 'name']

@admin.register(Invitees)
class InviteesAdmin(admin.ModelAdmin):

    list_display = ['id', 'event', 'owner']
    list_display_links = ['id', 'event',]



