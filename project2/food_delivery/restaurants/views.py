from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_location(request):
    return HttpResponse('Mahtumquli')

def get_phone(request):
    return HttpResponse('77-221-21-22')