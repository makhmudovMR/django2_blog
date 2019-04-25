from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        }
    return render(request, 'blog/index.html', context=context)


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    context={'post':post}
    return render(request, 'blog/post_detail.html', context=context)
