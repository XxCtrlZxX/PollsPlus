from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment


def index(request):
    return render(request, 'pollsplus/index.html')


# 게시글 보기
def posts(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:10]
    context = {'latest_posts': latest_post_list}
    return render(request, 'pollsplus/posts.html', context)


# 댓글 자세히 보기
def comments(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pollsplus/comments.html', {'post': post})


# 게시글 작성창
def posting(request):
    return render(request, 'pollsplus/posting.html')


# 작성된 게시글 업로드
def upload(request):
    try:
        title_text = request.POST['title']
        writer = request.POST['writer']
        contents = request.POST['contents']
    except KeyError:
        return render(request, 'pollsplus/posting.html',
                      {'error_message': 'KeyError: Upload is not successful. Please try again.'})

    post = Post(title_text=title_text, writer=writer, contents_text=contents)
    post.save()
    return HttpResponseRedirect(reverse('pollsplus:posts', args=()))
