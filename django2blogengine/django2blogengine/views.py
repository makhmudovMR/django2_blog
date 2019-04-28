from django.shortcuts import render, redirect, reverse

def redirect_blog(request):
    return redirect(reverse('posts_list'), permanent=True)