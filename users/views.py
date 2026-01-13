from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_name(request):
    return HttpResponse('Benedetta')

def get_age(request):
    return HttpResponse('25')