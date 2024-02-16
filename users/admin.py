from django.contrib import admin
from .models import Profile
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username', 'name', 'is_staff',]
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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'avatar']
    list_display_links = ['id', 'user']
    prepopulated_fields = {'slug': ('user',)}