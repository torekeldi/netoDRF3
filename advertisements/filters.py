from django_filters.rest_framework import DateFromToRangeFilter, FilterSet

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Advertisement
        fields = ['creator', 'status']
