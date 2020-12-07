from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect

@csrf_exempt
def signup(request):
    if request.method == "POST":
        userid = request.POST.get("userid", "")
        username = request.POST.get("username", "")
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if userid == "":
            return render(request, "accounts/signup.html", {"error": "input id"})

        if username == "":
            return render(request, "accounts/signup.html", {"error": "input name"})

        if password1 == "":
            return render(request, "accounts/signup.html", {"error": "input pw"})

        if password2 == "":
            return render(request, "accounts/signup.html", {"error": "input confirm pw "})

        if password1 == password2:
            user = User.objects.create_user(username=userid, password=password1, first_name=username)
            user.save()
            auth.login(request, user)
            return redirect("polls:accounts:index")

    return render(request, 'accounts/signup.html')

@csrf_exempt
def signin(request):
    if request.method == "POST":
        userid = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if userid == "":
            return render(request, "accounts/signin.html", {"error": "input id"})

        if password == "":
            return render(request, "accounts/signin.html", {"error": "input pw"})

        user = auth.authenticate(request, username=userid, password=password)

        if user is None:
            return render(request, 'accounts/signin.html', {"error": "username or password is incorrect"})
        else:
            auth.login(request, user)
            return render('accounts/index.html', {"userid": userid})
    return render(request, 'accounts/signin.html')

    return render(request, 'accounts/signin.html')


def signout(request):
    auth.logout(request)
    return render(request, "accounts/index.html")


def index(request):
    return render(request, 'accounts/index.html')
# Create your views here.
