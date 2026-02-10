from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Order, OrderItem
from cart.models import Cart
from django.contrib import messages


def create_order(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = Cart.objects.get(user=request.user)

    if not cart.items.exists():
        return JsonResponse({'error': 'Cart is empty'})

    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        order = Order.objects.create(
            user=request.user,
            total=cart.total_price(),
            address=address,
            phone=phone
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product_name=item.product.name,
                price=item.product.price,
                quantity=item.quantity
            )

            item.product.stock -= item.quantity
            item.product.save()

        cart.items.all().delete()

        return redirect('order_detail', order_id=order.id)

    return render(request, 'orders/create.html', {
        'cart': cart,
        'total': cart.total_price()
    })


def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('login')

    orders = Order.objects.filter(user=request.user)

    return render(request, 'orders/my_orders.html', {
        'orders': orders
    })


def order_detail(request, order_id):
    if not request.user.is_authenticated:
        return redirect('login')

    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.all()

    return render(request, 'orders/detail.html', {
        'order': order,
        'items': items
    })


def update_order_status(request, order_id):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Admin only'})

    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()

        return redirect('order_detail', order_id=order.id)

    return render(request, 'orders/update_status.html', {
        'order': order
    })


def cancel_order(request, order_id):
    if not request.user.is_authenticated:
        return redirect('login')

    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == 'pending':
        order.status = 'cancelled'
        order.save()
        return redirect('my_orders')
    else:
        return JsonResponse({'error': 'Can only cancel pending orders'})



def admin_all_orders(request):
    if not request.user.is_staff:
        messages.error(request, 'Admin access only!')
        return redirect('products_list')

    orders = Order.objects.all().order_by('-created_at')

    return render(request, 'orders/admin_orders.html', {
        'orders': orders
    })


def admin_order_detail(request, order_id):
    if not request.user.is_staff:
        messages.error(request, 'Admin access only!')
        return redirect('products_list')

    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f'Order status updated to {order.get_status_display()}!')
        else:
            messages.error(request, 'Invalid status!')

    return render(request, 'orders/admin_order_detail.html', {
        'order': order,
        'items': items,
        'status_choices': Order.STATUS_CHOICES
    })