from django.contrib import admin
from .domain.models import Chat, Message

admin.site.register(Chat)
admin.site.register(Message)