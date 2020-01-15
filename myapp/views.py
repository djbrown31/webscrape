import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
# from requests.compat import quote_plus
from . import models

# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
# BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = { 
        'search': search 
        }
    return render(request, 'myapp/new_search.html', stuff_for_frontend)
