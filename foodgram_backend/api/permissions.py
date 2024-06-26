from rest_framework import permissions


class IsAuthorOrAdminOnlyPermission(permissions.BasePermission):
    """Пермишен для доступа админу или автору рецепта."""

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or request.user.is_superuser)
