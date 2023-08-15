from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    created_at = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = (
            "id",
            "title",
            "description",
            "creator",
            "status",
            "created_at",
            "favorite_users",
        )

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user
        if "status" in data and data["status"] == AdvertisementStatusChoices.OPEN:
            open_ads_count = Advertisement.objects.filter(
                creator=user, status=AdvertisementStatusChoices.OPEN
            ).count()
            if open_ads_count >= 10:
                raise serializers.ValidationError(
                    "У вас не может быть более 10 открытых объявлений"
                )
        return data
