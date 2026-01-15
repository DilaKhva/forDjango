from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_title(request):
    return HttpResponse('1984')

def get_price(request):
    return HttpResponse('65000')