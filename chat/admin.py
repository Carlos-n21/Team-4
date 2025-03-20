from django.contrib import admin
from .models import ChatRoom  # Import your ChatRoom model

class ChatRoomAdmin(admin.ModelAdmin):
    # Customize what fields to display in the list view of the admin
    list_display = ('name', 'friendly_name', 'description')

# Register the model and the admin class
admin.site.register(ChatRoom, ChatRoomAdmin)