from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_name(request):
    return HttpResponse('Mubina Yasinova')

def avg_score(request):
    return HttpResponse('Her average score is 4.5')