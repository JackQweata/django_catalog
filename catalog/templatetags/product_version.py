from django import template
import os
from catalog.models import Version

register = template.Library()


@register.simple_tag
def lastversionproduct(product):
    version = Version.objects.order_by('-version_number').filter(product=product).first()
    return version if version else ''
