from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View

from .models import Post, Tag
from .forms import TagForm, PostForm

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

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form_create.html', context={'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect(new_post)
        return render(request, 'blog/post_form_create.html', context={'form': form})



class TagList(View):
    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tags': tags,
        }
        return render(request, 'blog/tags_list.html', context=context)

class TagCreate(View):

    def post(self, request):
        tf = TagForm(request.POST)
        if tf.is_valid():
            new_tag = tf.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': tf})

    def get(self, request):
        tf = TagForm()
        context = {
            'form': tf
        }
        return render(request, 'blog/tag_create.html', context=context)

class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        posts = tag.posts.all()
        context = {
            'tag': tag,
            'posts': posts
        }
        return render(request, 'blog/tag_detail.html', context=context)