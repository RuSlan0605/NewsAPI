from django.contrib import admin
from .models import CustomUser
from .models import Category, Post, Comment
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    #model = CustomUser
    list_display = ['id', 'email', 'username', 'name', 'is_staff',]
    list_display_links = ['username', ]
'''    fieldsets = UserAdmin.fieldsets + (
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
    )'''


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'owner', 'publish', 'status']
    list_display_links = ['id', 'title']
    list_filter = ['status', 'created', 'publish', 'owner']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'user', 'email', 'post', 'created',]
    list_display_links = ['id', 'name', 'user', 'email']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'comment']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']




