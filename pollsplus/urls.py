from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('posts/<int:post_id>/comments/', views.comments, name='comments'),
    path('posts/<int:post_id>/comments/add/', views.addComment, name='addcomments'),
    path('posting/', views.posting, name='posting'),
    path('posting/upload/', views.upload, name='upload'),
    path('accounts/', include('accounts.urls',  namespace='accounts'))
]

app_name = 'pollsplus'
