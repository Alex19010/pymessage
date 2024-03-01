from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Post, Comment
from friends.models import Friend
from .forms import PostForm, CommentForm


@login_required()
def friends_posts(request):
    user = request.user
    friends = user.user.values_list('friend__id')
    posts = Post.objects.filter(owner__id__in = friends)   
    search = request.GET.get("search")    
    if search is not None:
        posts = posts.filter(name__icontains=search)
 
    paginator = Paginator(posts, 1)
    posts = paginator.get_page(request.GET.get("page"))

    context = {
        "posts": posts,
    }
    return render(request, "posts/home.html", context)


@login_required()
def my_posts(request):
    user = request.user
    posts = Post.objects.filter(owner = user)
    search = request.GET.get("search")    
    if search is not None:
        posts = posts.filter(name__icontains=search)
 
    paginator = Paginator(posts, 1)
    posts = paginator.get_page(request.GET.get("page"))
    context = {
        "posts": posts,
    }
    return render(request, "posts/my_posts.html", context)


@login_required()
def add_remove_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    if post in user.favorites.all():
        user.favorites.remove(post)
    else:
        user.favorites.add(post)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('home')
    context = {
        "form": form,
    }
    return render(request, 'posts/create_new_post.html', context)


@login_required()
def comments_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm()
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'posts/comments.html', context)


@login_required
def create_comment_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.post = post
            comment.save()
    return redirect('comments', post_id=post.id)