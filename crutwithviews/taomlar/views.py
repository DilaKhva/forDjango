from django.shortcuts import render, redirect
from django.views import View
from .models import Meal
# Create your views here.

class ListView(View):
    def get(self, request):
        meals = Meal.objects.all()
        return render(request, 'indexmeal.html', {'meals': meals})


class DetailView(View):
    def get(self, request, pk):
        meal = Meal.objects.filter(id=pk).first()
        return render(request, 'detailmeal.html', {'meal': meal})


class CreateMeal(View):
    def get(self, request):
        return render(request, 'createmeal.html')

    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        calories = request.POST.get('calories')
        is_spicy = request.POST.get('is_spicy') == 'on'

        meal = Meal.objects.create(
            title=title,
            price=price,
            desc=desc,
            calories=calories,
            is_spicy=is_spicy
        )
        meal.save()
        return redirect('indexmeal')


class UpdateMeal(View):
    def get(self, request, pk):
        meal = Meal.objects.get(id=pk)
        return render(request, 'updatemeal.html', {'meal': meal})

    def post(self, request, pk):
        meal = Meal.objects.get(id=pk)
        meal.title = request.POST.get('title')
        meal.price = request.POST.get('price')
        meal.desc = request.POST.get('desc')
        meal.is_spicy = request.POST.get('is_spicy') == 'on'
        meal.calories = request.POST.get('calories')
        meal.save()
        return redirect('indexmeal')

class DeleteMeal(View):
    def get(self, request, pk):
        meal = Meal.objects.filter(id=pk).first()
        meal.delete()
        return redirect('indexmeal')