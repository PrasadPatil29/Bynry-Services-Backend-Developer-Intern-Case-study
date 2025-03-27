from django import template

register = template.Library()

@register.filter
def filter_pending(requests):
    return [request for request in requests if request.status == 'pending']

@register.filter
def filter_completed(requests):
    return [request for request in requests if request.status == 'completed']
