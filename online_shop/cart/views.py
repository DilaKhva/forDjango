from django.shortcuts import render, redirect
from .models import Cart, CartItem
from products.models import *


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total': total,
    })


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    cart, created = Cart.objects.get_or_create(user=request.user)

    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity
        )

    return redirect('view_cart')


def remove_from_cart(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = Cart.objects.get(user=request.user)
    CartItem.objects.filter(cart=cart, id=item_id).delete()

    return redirect('view_cart')


def clear_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = Cart.objects.get(user=request.user)
    cart.items.all().delete()

    return redirect('view_cart')


def update_quantity(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = Cart.objects.get(user=request.user)
    item = CartItem.objects.get(cart=cart, id=item_id)

    quantity = int(request.POST.get('quantity'))
    item.quantity = quantity
    item.save()

    return redirect('view_cart')