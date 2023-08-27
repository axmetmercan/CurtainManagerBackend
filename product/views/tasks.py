
from celery import shared_task
from ..models import Brand, Color, Category
from picture.models import Picture
import time


@shared_task
def first_task( serializer):
    pass

@shared_task
def count():
    for i in range(10):
        time.sleep(1)
        print(f'Waiting Celery:{i}')