from django import template

register = template.Library()


@register.inclusion_tag('commons/_messages.html')
def show_messages(messages):
    return {'messages': messages}
