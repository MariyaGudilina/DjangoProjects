from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post
from pprint import pprint


class NewsList(ListView):
    model = Post
    ordering = '-ti'
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        pprint(context)
        return context


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'
