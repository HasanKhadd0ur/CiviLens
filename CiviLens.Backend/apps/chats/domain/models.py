from django.db import models
from apps.users.domain.models import User
from core.models.base_model import BaseModel

class Chat(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chats"
    )
    
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
    
    
class Message(BaseModel):
    ROLE_CHOICES = (
        ("user", "User"),
        ("assistant", "Assistant"),
    )

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.CharField(max_length=20, choices=ROLE_CHOICES)
    content = models.TextField()
    metadata = models.JSONField(null=True, blank=True)  # tokens, context used, etc.

    def __str__(self):
        return f"{self.sender}: {self.content[:30]}"
