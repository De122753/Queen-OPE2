from django import template

register = template.Library()


@register.filter(name='format')
def format(value, fmt):
    return fmt.format(value)
