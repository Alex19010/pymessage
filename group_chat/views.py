from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import GroupChat, GroupMessage
from .utils import encrypt_chat_id, decrypt_chat_id


@login_required()
def group_chat(request):
    return render(request, 'group_chat/chat_group_chat.html')


@login_required()
def chat_view(request):
    group_chats = GroupChat.objects.filter(members=request.user)
    context = {
        "chats": group_chats
    }
    return render(request, 'group_chat/chat_group_chat.html', context)


@login_required()
def chat_one_view(request, chat_id):
    group_chats = GroupChat.objects.filter(members=request.user)
    chat = get_object_or_404(GroupChat, id=chat_id, members=request.user)

    code = encrypt_chat_id(chat_id=chat.id)
    context = {
        "chats": group_chats,
        "chat": chat,
        "members": list(chat.members.all())[:4],
        "link": f"http://127.0.0.1:8000/group_chats/group_chat/invite/{code}"
    }
    return render(request, 'group_chat/chat_group_chat_one.html', context)


@login_required
def save_message_view(request, chat_id):
    if request.method == 'POST':
        message_content = request.POST.get('message_content')
        # Создайте новое сообщение и сохраните его
        chat = get_object_or_404(GroupChat, id=chat_id)
        new_message = GroupMessage.objects.create(chat=chat, sender=request.user, content=message_content)
        new_message.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    # else:
    #     return redirect('error_page')  # Если метод запроса не POST, перенаправьте пользователя на страницу ошибки


@login_required
def add_to_group_by_invite_link(request, code):
    chat_id = decrypt_chat_id(encrypted_id=code)
    chat = get_object_or_404(GroupChat, id=chat_id)

    user = request.user
    chat.members.add(user)

    return redirect(request.META.get('HTTP_REFERER', '/'))