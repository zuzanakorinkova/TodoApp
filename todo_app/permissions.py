from rest_framework import permissions

class IsOwnerOrNoAccess(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        # we want to make sure, user can see only his object
        # objects return needs to be true
        return request.user == obj.user
        # obj.user - each obj gonna be tested
