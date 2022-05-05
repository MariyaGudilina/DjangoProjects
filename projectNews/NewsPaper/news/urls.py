from django.urls import path
from .views import NewsList, PostListSearch, NewDelete, UserTemplate
from .views import NewsDetail, create_news, NewUpdate


urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='new_detail'),
   path('search/', PostListSearch.as_view(), name='news_search'),
   path('create/', create_news, name='new_create'),
   path('<int:pk>/edit/', NewUpdate.as_view(), name='new_update'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
]
