from django.db import models
from django.contrib.auth.models import User

from item.models import Item


class Conversation(models.Model):
    item = models.ForeignKey(
        Item, related_name="conversations", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name="conversations")
    criado_em = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "-modified_at",
        ]


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(
        User, related_name="created_messages", on_delete=models.CASCADE
    )
