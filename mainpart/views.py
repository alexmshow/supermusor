from django.shortcuts import render, redirect
from posts.models import Post

from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import RegisterForm
from .myutils import _isEnglish


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created')[:5]
    return render(request, 'mainpart/index.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration.html', {'form': form})

def user(request, username):
    try:
        if not _isEnglish(username):
            return render(request, 'mainpart/404user.html')
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, 'mainpart/404user.html')
    data = {
        'user': user,
    }
    return render(request, 'mainpart/user.html', data)