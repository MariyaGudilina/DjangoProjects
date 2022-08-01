from django.urls import path
from .views import NewsList, PostListSearch, NewDelete, UserTemplate, CategoryList, add_subscribe, Index
from .views import NewsDetail, create_news, NewUpdate
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='new_detail'),
   path('search/', PostListSearch.as_view(), name='news_search'),
   path('create/', create_news, name='new_create'),
   path('category/', CategoryList.as_view(), name='news_category'),
   path('<int:pk>/edit/', NewUpdate.as_view(), name='new_update'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
   path('subscribe/<int:pk>/', add_subscribe, name='subscribe'),
   path('locale/', Index.as_view(), name='locale'),
]
