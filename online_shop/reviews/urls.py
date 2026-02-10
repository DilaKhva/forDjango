from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:product_id>/', views.create_comment, name='create_comment'),
    path('<int:comment_id>/update/', views.update_comment, name='update_comment'),
    path('<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('my-comments/', views.my_comments, name='my_comments'),
]