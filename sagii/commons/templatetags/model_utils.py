from django import template

register = template.Library()


@register.inclusion_tag('commons/pagination.html', takes_context=True)
def show_pagination(context):
    return {'page_obj': context['page_obj']}
