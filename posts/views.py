from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from friends.models import Friend


@login_required()
def home(request):
    user = request.user
    friends = user.user.values_list('friend__id')
    posts = Post.objects.filter(owner__id__in = friends)
    context = {
        "posts": posts,
    }
    return render(request, "posts/home.html", context)
