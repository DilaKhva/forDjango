from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Uy

# Create your views here.

class ListView(View):
    def get(self, request):
        houses = Uy.objects.all()
        return render(request, 'index.html', {'houses': houses})

class DetailView(View):
    def get(self, request, pk):
        uy = Uy.objects.filter(id=pk).first()
        return render(request, 'detail.html', {'uy': uy})

class CreateView(View):
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        location = request.POST.get('location')
        rooms = request.POST.get('rooms')
        floors = request.POST.get('floors')
        area = request.POST.get('area')
        has_garden = request.POST.get('has_garden') == 'on'

        uy = Uy.objects.create(
            location = location,
            rooms = rooms,
            floors = floors,
            area = area,
            has_garden = has_garden
        )
        uy.save()
        return redirect('index')

class UpdateView(View):
    def get(self, request, pk):
        uy = Uy.objects.filter(id=pk).first()
        return render(request, 'update.html', {'uy': uy})

    def post(self, request, pk):
        uy = Uy.objects.filter(id=pk).first()

        uy.location = request.POST.get('location')
        uy.rooms = request.POST.get('rooms')
        uy.floors = request.POST.get('floors')
        uy.area = request.POST.get('area')
        # uy.has_garden = request.POST.get('has_garden')
        uy.has_garden = bool(request.POST.get('has_garden'))
        uy.save()
        return redirect('index')


class DeleteView(View):
    def get(self, request, pk):
        uy = Uy.objects.filter(id=pk).first()
        uy.delete()
        return redirect('index')