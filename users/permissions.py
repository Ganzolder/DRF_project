from rest_framework import permissions


class IsModer(permissions.BasePermission):
    message = 'Adding not allowed.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsNotModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        request.user.groups.filter(name="moders").exists()
        return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwnerOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.groups.filter(name="moders").exists()
