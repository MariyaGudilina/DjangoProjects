from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect

from .models import Post, Category
from django.core.mail import send_mail


@receiver(post_save, sender=Post)
def post(sender, instance, *args, **kwargs):
    postCategory = instance.postCategory.all()

    for categoryCurrent in postCategory:
        users = Category.objects.filter(pk=categoryCurrent.id).values("subscribers")
        for i in users:
            send_mail(
                subject=f"{instance.title}",
                message=f"Здравствуй, {User.objects.get(pk=i['subscribers']).username}."
                f" Новая статья в твоём любимом разделе! \n "
                f" Cтатья: {instance.title}, Категория: {categoryCurrent.name} \n"
                f" Текст статьи: {instance.content[:50]} \n"
                f" Ссылка http://127.0.0.1:8000/news/{instance.id}",
                from_email='marija.utochkina@yandex.ru',
                recipient_list=[User.objects.get(pk=i['subscribers']).email],
            )

    return redirect('/news/')
