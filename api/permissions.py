from rest_framework import permissions

class CustomUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if request.user.is_staff:
                return True
            return False
        
class CommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        if request.method =='POST':
            if request.user.is_authenticated:
                return True
            return False
        
class PostPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if request.user.is_staff:
                return True
            return False

class CategoryPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        if request.method == 'POST':
            if request.user.is_staff:
                return True
            return False
        
class NewsPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        if request.method == 'POST':
            if request.user.is_staff:
                return True
            return False
        
 