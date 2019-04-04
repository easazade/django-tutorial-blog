from django.shortcuts import redirect, render
from django.http import HttpResponse

posts = [
    {
        'author': 'Alireza',
        'title': 'Blog Post',
        'content': 'First post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Ahamd',
        'title': 'Blog Post 2',
        'content': 'Second post Content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'Saman',
        'title': 'Blog Post 3',
        'content': 'Third post Content',
        'date_posted': 'August 29, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
