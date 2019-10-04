from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForms
from django.shortcuts import redirect

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
    if request.method =='POST':
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForms()
        return render(request, 'blog/Forms.html', {'form':form} )

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForms(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})