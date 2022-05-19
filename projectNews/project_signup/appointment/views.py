from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse, redirect
from django.template.loader import render_to_string
from django.views import View
from django.core.mail import send_mail, EmailMultiAlternatives
from datetime import datetime

from .models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # получаем наш html
        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )

 #       send_mail(
        #           subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
        #          # имя клиента и дата записи будут в теме для удобства
        #          message=appointment.message,  # сообщение с кратким описанием проблемы
        #         from_email='MarUtoch@yandex.ru',  # здесь указываете почту, с которой будете отправлять
        #   recipient_list=['mariya_gudilina@mail.ru', ]

    #     )
        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,  # это то же, что и message
            from_email='marija.utochkina@yandex.ru',
            to=['mariya_gudilina@mail.ru'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

        return redirect('appointment:make_appointment')


