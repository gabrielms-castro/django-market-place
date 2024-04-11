from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Item(models.Model):
    categoria = models.ForeignKey(
        Categoria, related_name="items", on_delete=models.CASCADE, default=1
    )
    nome = models.CharField(max_length=255)
    descrição = models.TextField(blank=True, null=True)
    preço = models.FloatField()
    imagem = models.ImageField(upload_to="item_images", blank=True, null=True)
    foi_vendido = models.BooleanField(default=False)
    criado_por = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
