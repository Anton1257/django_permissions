from django_filters import rest_framework as filters
from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = {"status": ["exact"], "created_at": ["range"]}
