from rest_framework.permissions import BasePermission, SAFE_METHODS
from users import choices as user_choices


class IsEmployerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user.user_type == user_choices.UserTypeChoices.Employer
        )


class IsEmployerAndOwner(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user.user_type == user_choices.UserTypeChoices.Employer
        )

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
