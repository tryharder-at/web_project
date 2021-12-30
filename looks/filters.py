import django_filters
from django_filters import CharFilter

from .models import *


class LookFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Look
        fields = '__all__'
        exclude = ['description', 'favourite']
