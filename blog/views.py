import re
from bs4 import BeautifulSoup
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required

import requests

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    count = int(request.COOKIES.get('count', 0)) + 1
    response = render(request, 'blog/post_list.html', {'posts': posts})
    response.set_cookie('count', count)
    return response

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post': post} )

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def forecast(request):
    API_Key ='13572a732749976ee03b91c0ff4656a6'
    city = "Tokyo,jp"

    url = 'http://api.openweathermap.org/data/2.5/forecast'
    query = {
        'units': 'metric',
        'q': city,
        'cnt': '1',
        'appid': API_Key
    }

    r = requests.get(url, params=query)
    weather = r.json()
    temp= weather['list'][0]['main']['temp']
    cond= weather['list'][0]['weather'][0]['main']
    # print("response", r.json())
    # print("response_list", weather['list'][1]['main']['main'])
    print("response_list", weather['list'][0]['main']['temp'])

    return render(request, 'blog/weather.html', {'city': city, 'temp': temp,  'cond': cond})
    




