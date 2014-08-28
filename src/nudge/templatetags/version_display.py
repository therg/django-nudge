from django import template

register = template.Library()


@register.filter
def change_type(value):
    #return VERSION_TYPE_LOOKUP[int(value)]
    return value
