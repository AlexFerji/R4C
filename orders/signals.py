from django.db.models import signals
from django.core.mail import send_mail
from django.db import Error
from smtplib import SMTPException


from .models import Order
from robots.models import Robot


def send_email(sender, instance, created, **kwargs):
    serial = instance.serial
    orders = Order.objects.select_related('customer').only('customer__email').filter(robot_serial=serial)
    for order in orders:
        try:
            send_mail(
                subject=f"Робот {serial} теперь в наличии!",
                message=f'''
                        Добрый день!
                        Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. 
                        Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами
                        ''',
                from_email='robot_company@robots.com',
                recipient_list=[order.customer.email])
            try:
                order.delete()
            except Error as exception:
                pass
        except SMTPException as exception:
            pass


signals.post_save.connect(send_email,Robot, dispatch_uid="send_email")
