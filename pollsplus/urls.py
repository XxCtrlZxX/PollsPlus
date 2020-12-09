from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('posts/<int:post_id>/comments/', views.comments, name='comments'),
    path('posts/<int:post_id>/comments/add/', views.addComment, name='addcomments'),
    path('posting/', views.posting, name='posting'),
    path('posting/upload/', views.upload, name='upload'),
]

app_name = 'pollsplus'
