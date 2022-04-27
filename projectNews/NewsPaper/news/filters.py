from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post
from django.forms import DateInput


class PostFilter(FilterSet):
    ti = DateFilter(
        lookup_expr='gt',
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
        }



class ArticlesFilter(FilterSet):
    categoryType = CharFilter(method='my_custom')

    class Meta:
        model = Post
        fields = ['categoryType']

    def my_custom(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
