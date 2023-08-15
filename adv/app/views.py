from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import UnauthenticatedUserThrottle, AuthenticatedUserThrottle


class AdvertisementViewSet(ModelViewSet):
    throttle_classes = [UnauthenticatedUserThrottle, AuthenticatedUserThrottle]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        elif self.action in ["destroy", "update", "partial_update"]:
            return [IsAdminUser]
        return []

    @action(detail=True, methods=["POST"])
    def add_to_favorites(self, request, pk=None):
        ad = self.get_object()
        if ad.creator != request.user:
            ad.favorite_users.add(request.user)
            return Response({"message": "Реклама добавлена в избранное."})
        else:
            return Response(
                {"message": "Вы не можете добавить свою рекламу в избранное."}
            )
