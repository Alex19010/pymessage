from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Case, When, BooleanField, Q

from .models import Friend, Application
from accounts.models import User


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


@login_required()
def applications_view(request):
    user = request.user
    applications = Application.objects.filter(Q(user=user) | Q(friend=user)).annotate(
        can_accept=Case(
            When(user=request.user, then=False),
            default=True,
            output_field=BooleanField()
        )
    )
    total_applications = len(applications)
    context = {
        'applications': applications,
        'total_applications': total_applications,
    }
    return render(request, 'friends/friends_list_applications.html', context)


@login_required()
def add_friend(request, user_id):
    friend = get_object_or_404(User, id = user_id)
    if Friend.objects.filter(user=request.user, friend=friend).exists():
        return redirect(request.META.get('HTTP_REFERER', '/'))  
    if request.user.id != user_id:
        try:
            Application.objects.create(user = request.user, friend = friend)
        except IntegrityError:
            pass
    return redirect(request.META.get('HTTP_REFERER', '/'))  


@login_required()
def remove_friend(request, friend_id):
    friend = get_object_or_404(Friend, id = friend_id)
    if request.user in [friend.user, friend.friend]:
        friend.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def accept_application(request, application_id):
    application = get_object_or_404(Application, id = application_id)
    Friend.objects.create(user = application.user, friend = application.friend)
    application.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def delete_application(request, application_id):
    application = get_object_or_404(Application, id = application_id)
    if request.user in [application.user, application.friend]:
        application.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))
