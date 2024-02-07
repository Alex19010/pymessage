from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def private_chat(request):
    return render(request, 'private_chat/chat_private_chat.html')


# @login_required
# def is_log(request):
#     pass