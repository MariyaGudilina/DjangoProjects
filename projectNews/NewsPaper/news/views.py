from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.core.mail import send_mail
# Create your views here.
from datetime import datetime

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from .models import Post
from .models import Category
from pprint import pprint
from .filters import PostFilter, ArticlesFilter

from .forms import NewForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import hello, send_mail_every_week, send_mail_post_save
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.utils.translation import gettext as _


class Index(View):
    def get(self, request):
        string = _('Hello word')

        return HttpResponse(string)


class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    ordering = 'name'
    template_name = 'category.html'
    context_object_name = 'category'


@login_required
def add_subscribe(request, pk):
    user = request.user
    selectedCat = Category.objects.get(pk=pk)
    selectedCat.subscribers.add(user)
    return render(request, 'subscribe.html', context={'user': user, 'selectedCat': selectedCat})


# Все новости
class NewsList(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-ti'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


# Хочу отфильтровать только по статье, чтобы потом сделать навигацию. Без ввода пользователя
def articles_list(request):
    filter_categoryType = ArticlesFilter(request.GET, queryset=Post.objects.all())
    context = render(request, 'articles.html', {'filter': filter_categoryType})
    return context


class ArticlesListSearch(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-ti'
    template_name = 'articles.html'
    context_object_name = 'articles'

    # Переопределяем функцию списка новостей
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticlesFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


# Поиск с формой
class PostListSearch(LoginRequiredMixin, ListView):
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
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


# Одна новость
class NewsDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}',
                        None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj


# Одна статья
class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'


# Создать новость
@permission_required('news.add_post')
def create_news(request):
    current_user = request.user
    if current_user.is_authenticated:
        form = NewForm()
        if request.method == 'POST':
            form = NewForm(request.POST)
#           date = datetime.strptime(request.POST['date'], '%Y-%m-%d')
            mail = current_user.email
            title = request.POST['title']
            text = request.POST['content']
            postCategory = request.POST['postCategory']
            cat = Category.objects.get(id=postCategory)
            users = cat.subscribers.all()
            if form.is_valid():
                categoryType = form.save(commit=False)
                categoryType.categoryType = 'NW'
                categoryType.save()
                '''
                if current_user in users:
                    send_mail(
                        subject=f'Hello, {current_user.username} . New article in your favorite section!».',
                        message=f'{text[:50]} \n'
                                f' Ссылка http://127.0.0.1:8000/news/{categoryType.id}',

                        from_email='marija.utochkina@yandex.ru',
                        recipient_list=[mail],
                    )
                '''
                send_mail_post_save.delay(categoryType.id)

                return HttpResponseRedirect('/news/')

        return render(request, 'new_edit.html', {'form': form})

    else:
        return HttpResponseRedirect('/news/')


# Создать статью
@permission_required('news.add_post')
def create_news1(request):
    current_user = request.user
    if current_user.is_authenticated:
        form = NewForm()
        if request.method == 'POST':
            form = NewForm(request.POST)
#           current_date = datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            mail = current_user.email
            title = request.POST['title']
            text = request.POST['content']
            postCategory = request.POST['postCategory']
            cat = Category.objects.get(id=postCategory)
            users = cat.subscribers.all()

            if form.is_valid():
                categoryType = form.save(commit=False)
                categoryType.categoryType = 'AR'
                categoryType.save()
                if current_user in users:
                    send_mail(
                        subject=f'Hello, {current_user.username} . New article in your favorite section!».',
                        message=f'{text[:50]}',
                        from_email='marija.utochkina@yandex.ru',
                        recipient_list=[mail],
                    )
            return HttpResponseRedirect('/news/')

        return render(request, 'article_edit.html', {'form': form})
    else:
        return HttpResponseRedirect('/news/')


class NewUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewForm
    model = Post
    template_name = 'new_edit.html'


class NewDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'new_delete.html'
    success_url = reverse_lazy('news_list')


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewForm
    model = Post
    template_name = 'article_edit.html'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')


class UserTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/default.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class IndexView(View):
    def get(self, request):
        # printer.apply_async([10], countdown=10)
        # hello.delay()
        send_mail_every_week.delay()
        return HttpResponse('Hello!')



