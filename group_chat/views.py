from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import GroupChat



@login_required()
def chat_view(request):
    private_chats = GroupChat.objects.filter(members=request.user)
    context = {
        "chats": private_chats
    }
    return render(request, 'private_chat/chat_private_chat.html', context)
