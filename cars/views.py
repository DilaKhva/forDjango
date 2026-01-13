from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_carname(request):
    return HttpResponse('BMW M5')

def get_price(request):
    return HttpResponse('120 000$')