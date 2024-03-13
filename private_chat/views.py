from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import PrivateChat, PrivateMessage
from accounts.models import User


@login_required()
def private_chat(request):
    return render(request, 'private_chat/chat_private_chat.html')


@login_required()
def chat_view(request):
    private_chats = PrivateChat.objects.filter(members=request.user)
    search = request.GET.get("search")
    if bool(search) != False:
        private_chats = private_chats.filter(members__first_name__icontains=search)
    context = {
        "chats": private_chats
    }
    return render(request, 'private_chat/chat_private_chat.html', context)


@login_required()
def chat_one_view(request, chat_id):
    private_chats = PrivateChat.objects.filter(members=request.user)
    chat = get_object_or_404(PrivateChat, id=chat_id, members=request.user)
    context = {
        "chats": private_chats,
        "chat": chat,
    }
    return render(request, 'private_chat/chat_private_chat_one.html', context)


@login_required
def create_priv_chat(request, user_id):
    user = request.user
    friend = get_object_or_404(User, id=user_id)
    chat = PrivateChat.objects.filter(members=user).filter(members=friend).first()
    if chat is not None:
        return redirect('one_private_chat', chat_id= chat.id)
    
    chat = PrivateChat.objects.create()
    chat.members.set([user, friend])
    return redirect('one_private_chat', chat_id=chat.id)


@login_required
def save_message_priv_view(request, chat_id):
    if request.method == 'POST':
        message_content = request.POST.get('message_content')
        chat = get_object_or_404(PrivateChat, id=chat_id)
        new_message = PrivateMessage.objects.create(chat=chat, sender=request.user, content=message_content)
        new_message.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
