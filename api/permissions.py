from rest_framework import permissions

class CustomUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_staff:
            return True
        else:
            return False
        
class CommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True
        else:
            return False
        
class PostPermission(permissions.BasePermission):

    def has_permission(self, request, view):

            if request.method == 'GET':
                return True
            if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                if request.user.is_staff:
                    return True
                else:
                    return False

class CategoryPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
                return True
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if request.user.is_staff:
                return True
            else:
                return False
        return  False
        
 