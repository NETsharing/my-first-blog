from django.shortcuts import render, HttpResponse
from .models import Post


def post_list(request):
    # return  HttpResponse('hello world')
    return render(request, 'blog/post_list.html', {})
