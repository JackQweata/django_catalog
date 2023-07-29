from django import template
from django.conf import settings
import os

register = template.Library()


@register.simple_tag
def mediapath(image_path):
    media_url = settings.MEDIA_URL
    return os.path.join(media_url, str(image_path))


@register.filter
def mediapatchteg(image_path):
    media_url = settings.MEDIA_URL
    return f"{media_url}{image_path}"
