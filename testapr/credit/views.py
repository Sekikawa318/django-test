from .models import CreditModel
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return render(request, "signup.html", {})
            return redirect("login")
        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザ名は既に登録されています．"})
        
    return render(request, "signup.html", {})
    

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return render(request, "login.html", {})
    return render(request, "login.html", {})

@login_required
def listfunc(request):
    object_list = CreditModel.objects.all()
    return render(request, "list.html", {"object_list": object_list})

def logoutfunc(request):
    logout(request)
    return redirect("login")

@login_required
def detailfunc(request, pk):
    object = get_object_or_404(CreditModel, pk=pk)
    print(object)
    return render(request, "detail.html", {"object": object})

class CreditCreate(CreateView):
    template_name = "create.html"
    model = CreditModel
    fields = ("title", "user", "creditstatus", "others")
    success_url = reverse_lazy("list")

def searchfunc(request):
    if request.method == "POST":
        pk = request.POST["pk"]
        object = get_object_or_404(CreditModel, pk=pk)
        return render(request, "detail.html", {"object": object})
    else:
        return render(request, "search.html", {})