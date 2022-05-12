import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from datetime import datetime

#from .models import Category, Post
from NewsPaper.news.models import Category, Post

logger = logging.getLogger(__name__)


# наша задача по выводу текста на экран
def my_job():
    #  Your job processing logic here...
    print('hello from job')
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
#           msg.send()

# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),
            # trigger=CronTrigger(day_of_week="mon", hour="08", minute="00"),
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")