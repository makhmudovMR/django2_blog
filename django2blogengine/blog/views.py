from django.shortcuts import render
from django.http import HttpResponse


def posts_list(request):
    context = {
        'name': 'Magomed',
        'names': ['John', 'Boris', 'Oleg']
        }
    return render(request, 'blog/index.html', context=context)
