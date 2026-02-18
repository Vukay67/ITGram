from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import *
from .forms import AuthenticationForm

def feed_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "index.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect("feed_page")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)
