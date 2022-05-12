from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect

from .models import Post, Category
from django.core.mail import send_mail


@receiver(post_save, sender=Post)
def post(sender, instance, *args, **kwargs):
    postCategory = instance.postCategory.all()
    print(postCategory)
    for categoryCurrent in postCategory:
        users = Category.objects.filter(pk=categoryCurrent.id).values("subscribers")
        for i in users:
            send_mail(
                subject=f"{instance.title}",
                message=f"Здравствуй, {User.objects.get(pk=i['subscribers']).username}."
                f" Новая статья в твоём любимом разделе! \n Заголовок статьи: {instance.title} \n"
                f" Текст статьи: {instance.text[:50]}",
                from_email='marija.utochkina@yandex.ru',
                recipient_list=[User.objects.get(pk=i['subscribers']).email],
            )

    return redirect('/news/')
