
from celery import shared_task
from ..models import Brand, Color, Category
from picture.models import Picture


@shared_task
def first_task( serializer):
    pass