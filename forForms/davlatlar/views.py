from django.shortcuts import render, redirect
from .models import *
from django.views import View
from .forms import DavlatForm

# Create your views here.

class ListView(View):
    def get(self, request):
        countries = Davlat.objects.all()
        return render(request, 'index.html', {'countries': countries})

class DetailView(View):
    def get(self, request, pk):
        country = Davlat.objects.get(id=pk)
        return render(request, 'detail.html', {'country': country})

class CreateView(View):
    def get(self, request):
        form = DavlatForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = DavlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html', {'form': form})

class UpdateView(View):
    def get(self, request, pk):
        country = Davlat.objects.get(id=pk)
        form = DavlatForm(instance=country)
        return render(request, 'update.html', {'form': form})

    def post(self, request, pk):
        country = Davlat.objects.get(id=pk)
        form = DavlatForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'update.html', {'form': form})

class DeleteView(View):
    def get(self, request, pk):
        country = Davlat.objects.get(id=pk)
        country.delete()
        return redirect('index')
