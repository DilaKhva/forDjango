from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Product, Category, SubCategory
from django.db.models import Q


def products_list(request):
    products = Product.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query)
        )
    categories = Category.objects.all()

    return render(request, 'products/list.html', {
        'products': products,
        'categories': categories,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.all()

    return render(request, 'products/detail.html', {
        'product': product,
        'comments': comments
    })



def add_product(request):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Admin only'})

    categories = Category.objects.all()
    subcategories = SubCategory.objects.none()

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        subcategory_id = request.POST.get('subcategory_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        stock = request.POST.get('stock')

        if not category_id or not subcategory_id or not name or not price:
            messages.error(request, "Please fill all required fields.")
            if category_id:
                subcategories = SubCategory.objects.filter(category_id=category_id)
            return render(request, 'products/add.html', {
                'categories': categories,
                'subcategories': subcategories
            })

        Product.objects.create(
            category_id=category_id,
            subcategory_id=subcategory_id,
            name=name,
            price=price,
            description=description,
            image=image,
            stock=stock or 0
        )
        messages.success(request, "Product added successfully!")
        return redirect('products_list')

    category_id = request.GET.get('category')
    if category_id:
        subcategories = SubCategory.objects.filter(category_id=category_id)

    return render(request, 'products/add.html', {
        'categories': categories,
        'subcategories': subcategories
    })


def edit_product(request, product_id):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Admin only'})

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.description = request.POST.get('description')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()
        return redirect('product_detail', product_id=product.id)

    categories = Category.objects.all()
    return render(request, 'products/edit.html', {
        'product': product,
        'categories': categories
    })


def delete_product(request, product_id):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Admin only'})

    product = get_object_or_404(Product, id=product_id)
    product.delete()

    return redirect('products_list')