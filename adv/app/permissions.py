from rest_framework.permissions import BasePermission
from rest_framework.throttling import UserRateThrottle


class UnauthenticatedUserThrottle(UserRateThrottle):
    rate = "10/minute"


class AuthenticatedUserThrottle(UserRateThrottle):
    rate = "20/minute"


class IsAdvertisementAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
