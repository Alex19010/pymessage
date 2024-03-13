from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import GroupChat, GroupMessage
from .utils import encrypt_chat_id, decrypt_chat_id
from .forms import GroupChatForm


@login_required()
def group_chat(request):
    return render(request, 'group_chat/chat_group_chat.html')


@login_required()
def chat_view(request):
    group_chats = GroupChat.objects.filter(members=request.user)
    search = request.GET.get("search")
    if bool(search) != False:
        group_chats = group_chats.filter(name__icontains=search)
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
        "members": list(chat.members.all())[:5],
        "link": f"http://127.0.0.1:8000/group_chats/invite/{code}"
    }
    return render(request, 'group_chat/chat_group_chat_one.html', context)


@login_required
def save_message_view(request, chat_id):
    if request.method == 'POST':
        message_content = request.POST.get('message_content')
        chat = get_object_or_404(GroupChat, id=chat_id)
        new_message = GroupMessage.objects.create(chat=chat, sender=request.user, content=message_content)
        new_message.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def add_to_group_by_invite_link(request, code):
    chat_id = decrypt_chat_id(encrypted_id=code)
    chat = get_object_or_404(GroupChat, id=chat_id)

    user = request.user
    chat.members.add(user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


# @login_required
# def create_group_chat(request):
#     form = GroupChatForm(request.POST)
#     if form.is_valid():
#         group = form.save()
#         group.members.add(request.user)
#         return redirect(request.META.get('HTTP_REFERER', '/'))
    

@login_required
def create_group_chat(request):
    form = GroupChatForm()
    if request.method == 'POST':
        form = GroupChatForm(request.POST)
        if form.is_valid():
            group = form.save()
            group.members.add(request.user)
            return redirect('group_chat')
    context = {
        "form": form,
    }
    return render(request, 'group_chat/chat_group_new_group_chat.html', context)


@login_required
def update_group_chat(request, chat_id):
    chat = get_object_or_404(GroupChat, id = chat_id)
    form = GroupChatForm(instance=chat)
    if request.method == 'POST':
        form = GroupChatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_chat')
    context = {
        "form": form,
    }
    return render(request, 'group_chat/chat_group_new_group_chat.html', context)