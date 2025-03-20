from django.shortcuts import render
from .models import ChatRoom

def chat(request):
    chatrooms = ChatRoom.objects.all()  # Get all chatrooms
    return render(request, "chat/chat.html", {'chatrooms': chatrooms})


def chatroom(request, room_name):
    available_rooms = ChatRoom.objects.values_list('name', flat=True)
    chatroom = ChatRoom.objects.filter(name=room_name).first()

    chatroom_exists = room_name in available_rooms

    if not chatroom_exists:
        return render(request, "chat/chatroom_not_found.html", {"room_name": room_name})
    
    return render(request, "chat/chatroom.html", {
        "room_name": room_name,
        "friendly_name": chatroom.friendly_name,
    })
    