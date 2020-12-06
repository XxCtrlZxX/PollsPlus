from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment


def index(request):
    return render(request, 'pollsplus/index.html')


def posts(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    context = {'latest_posts': latest_post_list}
    return render(request, 'pollsplus/posts.html', context)


def comments(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pollsplus/comments.html', {'post': post})
