from rest_framework.permissions import BasePermission
from .models import User

'--------------------------------------------------------------------------------------------------'
    
class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.ADMIN
    
class IsNewsEditor(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.NEWS_EDITOR