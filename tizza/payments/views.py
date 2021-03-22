from django.http import JsonResponse
from django.shortcuts import render


def index(request) -> JsonResponse:
    """Método de exibição do pagamento.

    Args:
        request: Objeto request django.

    Returns: Reposta com os objetos encontrados.
    """

    if request.method == "GET":
        data = {
            'content': 'Acesso bem sucedido'
        }
        return JsonResponse(data)
