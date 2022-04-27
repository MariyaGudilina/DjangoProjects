from django.urls import path
from .views import NewsList, PostListSearch, NewDelete, ArticlesListSearch
from .views import NewsDetail, create_news1, NewUpdate


urlpatterns = [
   path('', ArticlesListSearch.as_view(), name='articles_list'),
#   path('<int:pk>', NewsDetail.as_view(), name='new_detail'),
#   path('search/', PostListSearch.as_view(), name='news_search'),
   path('create/', create_news1, name='articles_create'),
   path('<int:pk>/edit/', NewUpdate.as_view(), name='articles_update'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='articles_delete'),
]
