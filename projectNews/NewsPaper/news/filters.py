from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post
from django.forms import DateInput


# Фильтр для поиска с формой
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


# Нужен простой фильтр, как задать без формы
class ArticlesFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'categoryType': ['exact'],
        }


