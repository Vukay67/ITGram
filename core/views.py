from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import AuthenticationForm, RegistrationForm

@login_required
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

def register_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = User.objects.create_user(
                email=email,
                username=username,
                password=password
            )
            login(request, user)
            return redirect("feed_page")
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)