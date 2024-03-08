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
    search = request.GET.get("search")
    if bool(search) != False:
        friends = friends.filter(friend__first_name__icontains=search)
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
    users_applications = Application.objects.filter(Q(friend=user)).annotate(
        can_accept=Case(
            When(user=request.user, then=False),
            default=True,
            output_field=BooleanField()
        )
    )
    my_applications = Application.objects.filter(Q(user=user)).annotate(
        can_accept=Case(
            When(user=request.user, then=False),
            default=True,
            output_field=BooleanField()
        )
    )
    search_users = None
    search = request.GET.get("search")
    if bool(search) != False:
        search_users = User.objects.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search)
            ).exclude(
                id__in=applications.values_list('friend_id')
            ).exclude(
                id=user.id
            ).exclude(
                id__in=Friend.objects.filter(user=user).values_list('friend_id')
            )

    total_applications = len(applications)
    context = {
        'applications': applications,
        'users_applications': users_applications,
        'my_applications': my_applications,
        'total_applications': total_applications,
        'search_users': search_users
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
            print('test')
        except IntegrityError:
            pass
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def remove_friend(request, friend_id):
    friend = get_object_or_404(Friend, id = friend_id)
    reversed_friend = get_object_or_404(Friend, user = friend.friend.id, friend = friend.user.id)
    if request.user in [friend.user, friend.friend]:
        friend.delete()
        reversed_friend.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def accept_application(request, application_id):
    application = get_object_or_404(Application, id = application_id)
    Friend.objects.create(user = application.user, friend = application.friend)
    Friend.objects.create(user = application.friend, friend = application.user)
    application.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def delete_application(request, application_id):
    application = get_object_or_404(Application, id = application_id)
    if request.user in [application.user, application.friend]:
        application.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))
