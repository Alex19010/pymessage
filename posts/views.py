from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from friends.models import Friend
from .forms import PostForm


@login_required()
def home(request):
    user = request.user
    friends = user.user.values_list('friend__id')
    posts = Post.objects.filter(owner__id__in = friends)
    context = {
        "posts": posts,
    }
    return render(request, "posts/home.html", context)


@login_required()
def add_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    if user in post.owner.favorites.all():
        post.owner.favorites.remove(post)
    else:
        post.owner.favorites.add(post)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            group = form.save()
            group.members.add(request.user)
            return redirect('home')
    context = {
        "form": form,
    }
    return render(request, 'posts/create_new_post.html', context)
