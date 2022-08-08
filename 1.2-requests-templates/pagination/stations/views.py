import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf=8') as csvfile:
        info = csv.DictReader(csvfile)
        list_info = list(info)
    current_page = request.GET.get('page', 1)
    paginator = Paginator(list_info, 10)
    page = paginator.get_page(current_page)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
