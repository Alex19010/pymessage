from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import PrivateChat, PrivateMessage


@login_required()
def private_chat(request):
    return render(request, 'private_chat/chat_private_chat.html')


# def chat_view(request):
#     Chat = PrivateChat
#     Messages = PrivateMessage
#     user_chats = Chat.objects.filter(members=request.user)  # Получаем все чаты пользователя
#     messages = []
#     for chat in user_chats:
#         chat_messages = chat.Messages.all()  # Получаем все сообщения для каждого чата
#         messages.extend(chat_messages)
#     messages = sorted(messages, key=lambda x: x.timestamp)  # Сортируем сообщения по времени
#     return render(request, 'chat.html', {'messages': messages})


def chat_view(request):
    private_chats = PrivateChat.objects.filter(members=request.user)
    messages = PrivateMessage.objects.filter(chat__in=private_chats).order_by('timestamp')
    return render(request, 'chat.html', {'messages': messages})