from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm

def index(request):
    return render(request, 'pollsplus/index.html')


# 게시글 보기
def posts(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:10]
    context = {'latest_posts': latest_post_list}

    if request.method == "POST":
        id = request.POST["id"]
        post = Post.objects.all().filter(id=id)
        post.delete()
        return redirect("pollsplus:index")
        
    return render(request, 'pollsplus/posts.html', context)

# 댓글 자세히 보기
def comments(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pollsplus/comments.html', {'post': post})


# 댓글 작성, 업로드
def addComment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        writer = request.POST['writer']
        contents = request.POST['contents']
    except KeyError:
        return render(request, 'pollsplus/comments.html', {
            'post': post,
            'error_message': 'Upload is not successful. Please try again.'
        })
    comment = Comment(writer=writer, contents_text=contents)
    comment.post = post
    comment.save()
    return HttpResponseRedirect(reverse('pollsplus:comments', args=(post.id, )))


# 게시글 작성창
def posting(request):
    return render(request, 'pollsplus/posting.html')


# 작성된 게시글 업로드
def upload(request):
    try:
        title_text = request.POST['title_text']
        writer = request.POST['writer']
        contents = request.POST['contents']

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.title_text = title_text
            post.writer = writer
            post.contents = contents
            post.save()
        else:
            post = Post(title_text=title_text, writer=writer, contents_text=contents)
            post.save()
    except KeyError:
        return render(request, 'pollsplus/posting.html',
                      {'error_message': 'Upload is not successful. Please try again.'})

    return HttpResponseRedirect(reverse('pollsplus:posts', args=()))

def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        post.title_text = request.POST.get("title_text", "")
        post.writer = request.POST.get("writer", "")
        post.contents_text = request.POST.get("contents", "")
        post.update()
        return render(request, 'pollsplus/posting.html',
                      {'error_message': '수정이 완료되었습니다.'})

    return render(request, 'pollsplus/edit.html', {'post': post})