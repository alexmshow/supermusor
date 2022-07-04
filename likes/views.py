from django.shortcuts import render

# LIKES
def index(request):
    return render(request, 'likes/base.html')