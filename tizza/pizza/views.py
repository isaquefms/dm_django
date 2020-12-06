from django.http import HttpResponse

from .models import Pizza


def index(request, p_id: int) -> HttpResponse:
    """Define a interface de acesso a um objeto pizza.

    Args:
        request: Request padrão django.
        p_id: ID do objeto pesquisado.

    Returns: Resposta Http.
    """
    try:
        pizza = Pizza.objects.get(id=p_id)
    except Pizza.DoesNotExist:
        return HttpResponse(content={
            'status': 'error',
            'msg': 'Objeto não encontrado',
        })
    return HttpResponse(content={
        'id': pizza.id,
        'title': pizza.title,
        'description': pizza.description,
    })


def random(request) -> HttpResponse:
    """Define a interface de acesso a um objeto aleatório.

    Args:
        request: Requisição padrão Django.

    Returns: Resposta Http.
    """
    # obtendo objeto aleatório
    try:
        pizza = Pizza.objects.all().order_by('?')[0]
        return HttpResponse(content={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        })
    except IndexError:
        return HttpResponse(content={
            'status': 'error',
            'msg': 'Objeto não encontrado',
        })
