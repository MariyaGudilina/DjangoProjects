from django.urls import path
from .views import UserTemplate

urlpatterns = [
    path('', UserTemplate.as_view())
]