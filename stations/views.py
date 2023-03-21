from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    data = []
    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    paginator = Paginator(data, 25)
    bus_stations = paginator.get_page(page_number)
    context = {
        'bus_stations': bus_stations,
    }
    return render(request, 'stations/index.html', context)
