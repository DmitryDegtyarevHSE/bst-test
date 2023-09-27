from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from .models import Robot
from .services import get_customers_list, send_notifications


@receiver(signal=post_save, sender=Robot)
def notify_customer(instance, **kwargs):
    print("сработал сигнал")
    customers = get_customers_list(serial=instance.serial)
    if customers:
        try:
            send_notifications(instance.serial, settings.EMAIL_HOST_USER, customers)
        except ValueError:
            pass
