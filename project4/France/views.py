from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello from France!")

def where_is_it(request):
    return HttpResponse('Which city in France?\n- in Paris!')