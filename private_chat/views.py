from django.shortcuts import render


def private_chat(request):
    return render(request, 'private_chat/chat_private_chat.html')
