from django.contrib import admin
from .models import Category, Post, Comment, News


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'owner', 'status']
    list_display_links = ['id', 'title']
    list_filter = ['status', 'created', 'updated', 'owner']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ['status', 'created']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'image']
    list_display_links = ['id', 'title']
    list_filter = ['title']

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
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']




