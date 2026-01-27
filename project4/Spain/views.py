from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def spain(request):
    return HttpResponse('I am not in pain, I am in Spain!')

def where_is_it(request):
    return HttpResponse('Hello from Madrid')