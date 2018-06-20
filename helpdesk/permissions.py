from rest_framework.permissions import BasePermission

class ExecutorPermission(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.has_perm('helpdesk.can_close')

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.has_perm('helpdesk.can_add_change')
