from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def index(request):
    data = Product.objects.all()
    context = {
        'products': data,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        created_date = request.POST['created_date']
        expire_date = request.POST['expire_date']
        desc = request.POST['desc']
        amount = request.POST['amount']

        dori = Product.objects.create(
            title = title,
            price = price,
            created_date = created_date,
            expire_date = expire_date,
            desc = desc,
            amount = amount,
        )
        dori.save()
        return redirect('index')
    return render(request, 'create_product.html')

def update(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.title = request.POST['title']
        product.price = request.POST['price']
        product.created_date = request.POST['created_date']
        product.expire_date = request.POST['expire_date']
        product.desc = request.POST['desc']
        product.amount = request.POST['amount']
        product.save()
        return redirect('index')
    return render(request, 'update_product.html', {'product': product})

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('index')