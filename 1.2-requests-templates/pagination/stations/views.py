from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.paginator import Paginator
import csv
from pagination.settings import BUS_STATION_CSV

def index(request):

    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(BUS_STATION_CSV, 'r', encoding='UTF-8') as filecsv:
        stations = [line_dir for line_dir in csv.DictReader(filecsv)]

    CONTENT = stations
    paginator = Paginator(CONTENT, 10)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)

    context = {
            'bus_stations': page.object_list,
            'page': page,
    }   

    return render(request, 'stations/index.html', context)