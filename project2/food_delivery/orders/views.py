from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_order_list(request):
    return HttpResponse('1. Norin 2. Manti 3. Osh')

def get_total_price(request):
    return HttpResponse('200000')