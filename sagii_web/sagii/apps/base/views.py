from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    import locale, calendar
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    return HttpResponse(', '.join(list(calendar.day_name)))