from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Friend


@login_required()
def friends_view(request):
    user = request.user
    friends = Friend.objects.filter(user=user)
    total_friends = len(friends)
    context = {
        'friends': friends,
        'total_friends': total_friends,
    }
    return render(request, 'friends/friends_list_friends.html', context)