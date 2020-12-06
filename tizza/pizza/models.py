from django.db import models
from django.contrib.auth import get_user_model


class Pizzeria(models.Model):
    """Classe para representar o objeto pizzaria.

    Attrs:
        owner(models.ForeignKey): Usuário dono da pizzaria.
        address(models.CharField): Endereço.
        phone(models.CharField): Telefone.
    """
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)


class Pizza(models.Model):
    """Classe representando o objeto pizza.

    Attrs:
        title (models.CharField): Título da pizza.
        description (models.CharField): Descrição da pizza.
    """
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)


class Likes(models.Model):
    """Classe para representar o objeto de curtidas.

    Attrs:
        user(models.ForeignKey): Usuário.
        pizza(models.ForeignKey): Pizza.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
