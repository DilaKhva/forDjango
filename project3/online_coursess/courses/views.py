from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_course_name(request):
    return HttpResponse("Python Backend course")

def get_course_price(request):
    return HttpResponse("150$")