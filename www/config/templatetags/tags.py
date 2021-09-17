from django.template import Library
from django.conf import settings

register = Library()

@register.simple_tag
def define(value=None):
    return value


@register.simple_tag
def site_info(key):
    allowed_key = []
    
    for k in settings.SITE_INFO.keys():
        allowed_key.append(k)

    allowed_key = ', '.join(allowed_key)

    try:
        info = settings.SITE_INFO[key]
    except KeyError:
        raise Exception(f"Key not allowed. Please use the following choices: {allowed_key}.")
    return info
