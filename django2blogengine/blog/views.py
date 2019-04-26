from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View

class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
            }
        return render(request, 'blog/index.html', context=context)


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        context={'post':post}
        return render(request, 'blog/post_detail.html', context=context)


class TagList(View):
    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tags': tags,
        }
        return render(request, 'blog/tags_list.html', context=context)



class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        posts = tag.posts.all()
        context = {
            'tag': tag,
            'posts': posts
        }
        return render(request, 'blog/tag_detail.html', context=context)
