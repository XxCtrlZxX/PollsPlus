from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is PollsPlus Index")


def posts(request):
    # return render(request, 'pollsplus/posts.html')
    return HttpResponse("This is PollsPlus Posts")
