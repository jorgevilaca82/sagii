from django import template
import collections
register = template.Library()

@register.filter(name='add_attributes')
def addcss(field, css):
    try:
        attrs = collections.defaultdict(str)
        definition = css.split(',')
        for d in definition:
            if ':' not in d:
                attrs['class'] += " %s"%d
            else:
                t, v = d.split(':')
                attrs[t] = v
        return field.as_widget(attrs=attrs)
    except Exception as e:
        return field