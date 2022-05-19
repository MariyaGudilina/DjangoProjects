from celery import shared_task
import time
from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string

from news.management.commands.runapscheduler import my_job
from news.signals import post
from news.models import Category, Post


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")


@shared_task
def send_mail_every_week():
    #    time.sleep(10)
    #    print("Отправка письма")
    my_job()


@shared_task
def send_mail_post_save(oid):
    postInstance = Post.objects.get(pk=oid)
    postCategory = postInstance.postCategory.all()
    print(postInstance.title)

    for categoryCurrent in postCategory:
        users = Category.objects.filter(pk=categoryCurrent.id).values("subscribers")
        for i in users:
            send_mail(
                subject=f"{postInstance.title}",
                message=f"Здравствуй, {User.objects.get(pk=i['subscribers']).username}."
                        f" Новая статья в твоём любимом разделе! \n "
                        f" Cтатья: {postInstance.title}, Категория: {categoryCurrent.name} \n"
                        f" Текст статьи: {postInstance.content[:50]} \n"
                        f" Ссылка http://127.0.0.1:8000/news/{postInstance.id}",
                from_email='marija.utochkina@yandex.ru',
                recipient_list=[User.objects.get(pk=i['subscribers']).email],
            )

    return redirect('/news/')





'''
    for category in Category.objects.all():
        news_from_each_category = []
        week_number_last = datetime.now().isocalendar()[1] - 1
        for news in Post.objects.filter(category_id=category.id,
                                            dateCreation__week=week_number_last).values('pk',
                                                                                        'title',
                                                                                        'ti',
                                                                                        'postCategory'):
            date_format = news.get("ti").strftime("%m/%d/%Y")
            new = (f' http://127.0.0.1:8000/news/{news.get("pk")}, {news.get("title")}, '
                       f'Категория: {news.get("category_id__name")}, Дата создания: {date_format}')
            news_from_each_category.append(new)

        subscribers = category.subscribers.all()
        for subscriber in subscribers:
            html_content = render_to_string(
                'subscribe.html', {'user': subscriber,
                                       'text': news_from_each_category,
                                       'category_name': category.name,
                                       'week_number_last': week_number_last})
            msg = EmailMultiAlternatives(
                subject=f'Здравствуй, {subscriber.username}, новые статьи за прошлую неделю в вашем разделе!',
                    from_email='marija.utochkina@yandex.ru',
                    to=[subscriber.email],
                )
            msg.attach_alternative(html_content, 'text/html')
            print(html_content)
            msg.send()
'''
