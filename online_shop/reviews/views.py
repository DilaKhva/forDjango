from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comment
from products.models import Product


def create_comment(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        text = request.POST.get('text')

        Comment.objects.create(
            product=product,
            user=request.user,
            text=text
        )

        messages.success(request, 'Comment posted successfully!')
        return redirect('product_detail', product_id=product.id)

    return render(request, 'reviews/create.html', {
        'product': product
    })


def update_comment(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('login')

    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        messages.error(request, 'You can only edit your own comments!')
        return redirect('product_detail', product_id=comment.product.id)

    if request.method == 'POST':
        comment.text = request.POST.get('text')
        comment.save()

        messages.success(request, 'Comment updated successfully!')
        return redirect('product_detail', product_id=comment.product.id)

    return render(request, 'reviews/update.html', {
        'comment': comment
    })


def delete_comment(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('login')

    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete this comment!')
        return redirect('product_detail', product_id=comment.product.id)

    product_id = comment.product.id
    comment.delete()

    messages.success(request, 'Comment deleted successfully!')
    return redirect('product_detail', product_id=product_id)


def my_comments(request):
    if not request.user.is_authenticated:
        return redirect('login')

    comments = Comment.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'reviews/my_comments.html', {
        'comments': comments
    })