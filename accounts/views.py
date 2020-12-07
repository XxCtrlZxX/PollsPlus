from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect


def signup(request):
    if request.method == "POST":
        userid = request.POST.get("userid", None)
        username = request.POST.get("username", None)
        password1 = request.POST.get("password1", None)
        password2 = request.POST.get("password2", None)

        if userid is None:
            return render(request, "accounts/signup.html", {"error": "input id"})

        if username is None:
            return render(request, "accounts/signup.html", {"error": "input name"})

        if password1 is None:
            return render(request, "accounts/signup.html", {"error": "input pw"})

        if password2 is None:
            return render(request, "accounts/signup.html", {"error": "input confirm pw "})

        if password1 == password2:
            user = User.objects.create_user(userid=userid, password=password1, username=username)
            user.save()
            auth.login(request, user)
            return render('accounts/index.html', {"userid": userid})
    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == "POST":
        userid = request.POST["userid"]
        password = request.POST["password"]
        if userid is None:
            return render(request, "accounts/signin.html", {"error": "input id"})

        if password is None:
            return render(request, "accounts/signin.html", {"error": "input pw"})

        user = auth.authenticate(request, userid=userid, password=password)
        if user is None:
            return render(request, 'accounts/signin.html', {"error": "username or password is incorrect"})
        else:
            auth.login(request, user)
            return render('accounts/index.html', {"userid": userid})


def signout(request):
    auth.logout(request)
    return render(request, "accounts/index.html")


def index(request):
    render(request, 'accounts/index.html')
# Create your views here.
