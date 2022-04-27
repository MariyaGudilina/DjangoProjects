from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post
from .models import Category
from pprint import pprint
from .filters import PostFilter, ArticlesFilter

from .forms import NewForm


class NewsList(ListView):
    model = Post
    ordering = '-ti'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        pprint(context)
        return context



def articles_list(request):
    filter = ArticlesFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'articles.html',{'filter': filter})


class ArticlesListSearch(ListView):
    model = Post
    ordering = '-ti'
    template_name = 'articles.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticlesFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostListSearch(ListView):
    model = Post
    ordering = '-ti'
    template_name = 'newsSearch.html'
    context_object_name = 'posts'

    # Переопределяем функцию списка новостей
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'


def create_news(request):
    form = NewForm()
    if request.method == 'POST':

        form = NewForm(request.POST)

        if form.is_valid():
            categoryType = form.save(commit=False)
            categoryType.categoryType = 'NW'
            categoryType.save()

            return HttpResponseRedirect('/news/')

    return render(request, 'new_edit.html', {'form': form})


def create_news1(request):
    form = NewForm()
    if request.method == 'POST':

        form = NewForm(request.POST)

        if form.is_valid():
            categoryType = form.save(commit=False)
            categoryType.categoryType = 'AR'
            categoryType.save()

            return HttpResponseRedirect('/news/')

    return render(request, 'article_edit.html', {'form': form})


class NewUpdate(UpdateView):
    form_class = NewForm
    model = Post
    template_name = 'new_edit.html'


class NewDelete(DeleteView):
    model = Post
    template_name = 'new_delete.html'
    success_url = reverse_lazy('news_list')
