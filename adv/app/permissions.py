from rest_framework.throttling import UserRateThrottle


class UnauthenticatedUserThrottle(UserRateThrottle):
    rate = "10/minute"


class AuthenticatedUserThrottle(UserRateThrottle):
    rate = "20/minute"
