from django.urls import path
from .views import NewDelete, ArticlesListSearch, ArticleDetail, ArticleUpdate, ArticleDelete
from .views import create_news1, NewUpdate


urlpatterns = [
   path('', ArticlesListSearch.as_view(), name='articles_list'),
   path('<int:pk>', ArticleDetail.as_view(), name='articles_detail'),
#   path('search/', PostListSearch.as_view(), name='news_search'),
   path('create/', create_news1, name='articles_create'),
   path('<int:pk>/edit/', ArticleUpdate.as_view(), name='articles_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='articles_delete'),
]
