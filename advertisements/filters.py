from django_filters import rest_framework as filters
from django.contrib.auth.models import User

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    creator = filters.ModelMultipleChoiceFilter(
        field_name='creator',
        to_field_name='id',
        queryset=User.objects.all(),
    )
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ('creator', 'status', 'created_at')
