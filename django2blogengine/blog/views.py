from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

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


def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'blog/tags_list.html', context=context)

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    posts = tag.posts.all()
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/tag_detail.html', context=context)