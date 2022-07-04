from django.shortcuts import render, redirect

from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from .forms import PostForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.models import Post


@login_required
def create(request):
    errors = '1'
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('../')
        else:
            errors = form.errors.as_data()
    
    form = PostForm()

    if errors == "1":
        data = {
        'form': form,
        'errors': ""
        }
    else:
        data = {
        'form': form,
        'errors': str(list(errors.values())[0][0])[2:len(str(list(errors.values())[0][0]))-3]
        }
    return render(request, 'posts/create.html', data)

def lazy_load_posts(request):
    page = request.POST.get('page')
    posts = Post.objects.order_by('-created')
  
    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 5
    paginator = Paginator(posts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # build a html posts list with the paginated posts
    posts_html = loader.render_to_string('mainpart/posts.html', {'posts': posts})

    # package output data and return it as a JSON object
    output_data = {'posts_html': posts_html, 'has_next': posts.has_next()}
    return JsonResponse(output_data)