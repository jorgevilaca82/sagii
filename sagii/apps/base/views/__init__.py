from django.views import generic
from django.http import HttpResponse
from . import pessoafisica
from . import pessoajuridica

def _index(request):
    import locale
    import calendar
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    return HttpResponse(', '.join(list(calendar.day_name)))


class HomeView(generic.TemplateView):
    template_name = "base/home.html"