from django.urls import path
from .views import home, createpost, post_list, post_detail, update_post, delete_post

urlpatterns = [
    path('homepage/', home),
    path('create/', createpost, name = 'createpost'),
    path('posts/', post_list, name="post_list"),
    path('post/<int:post_id>/', post_detail, name="post_detail"),  # Dynamic URL
    path('post/<int:post_id>/update/', update_post, name="update_post"),  # Update URL
    path('post/<int:post_id>/delete/', delete_post, name="delete_post"),  # Delete URL
]