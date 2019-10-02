from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForms


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_trust(request):
    return render(request, 'blog/base.html', {})
def post_detail(request, pk):
    post =get_object_or_404(Post, pk=pk)
    # post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
def post_new(request):
    form = PostForms()
    return render(request, 'blog/Forms.html', {'form':form} )