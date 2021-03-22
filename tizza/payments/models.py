from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

from ..pizza.models import Pizzeria


class Payment(models.Model):
    """Pagamento de um usuário pelo uso de um determinado estabelecimento.

    Attrs:
        user(models.ForeignKey): usuário quem executa o pagamento.
        pizzaria(models.ForeignKey): estabelecimento que gerou o pagamento.
        value(models.DecimalField): valor do pagamento realizado.
    """

    user = models.ForeignKey(get_user_model(), verbose_name='User', on_delete=models.PROTECT)
    pizzeria = models.ForeignKey(Pizzeria, verbose_name='Pizzaria', on_delete=models.PROTECT)
    value = models.DecimalField('Value', max_digits=10, decimal_places=4)
    date = models.DateTimeField('Payment date', auto_now=True)

    def __str__(self) -> str:
        if self.pk is not None:
            return f'Payment: {self.pk}, from user: {self.user.name} of establishment {self.pizzeria.name}'
        return ''

    @staticmethod
    def get_user_payments(user_id: int) -> QuerySet:
        """Obtém todos os pagamentos realizados pelo usuário.

        Args:
            user_id: ID do usuário.

        Returns: Pagamentos do usuário.
        """
        return Payment.objects.filter(user_id=user_id).order_by('-date')
