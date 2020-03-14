from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForms
from .models import Post

# Create your views here.

def home (request):
    posts = Post.objects.all()
    return render(request, 'home.html', {"posts" : posts})

def new(request):
    if request.method =="POST":
        form = PostForms(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            form.save()
            return redirect('detail', post.pk)
    else:
        form = PostForms()
    return render(request, 'new.html', {"form" : form})    

def detail(request, post_pk):
    # post = Post.objects.get(pk=post_pk)
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'detail.html', {"post" : post})
