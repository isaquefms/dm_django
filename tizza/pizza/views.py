import json

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required

from .models import Pizza, Likes


@login_required
def index(request, p_id: int) -> JsonResponse:
    """Define a interface de acesso a um objeto pizza.

    Args:
        request: Request padrão django.
        p_id: ID do objeto pesquisado.

    Returns: Resposta Http.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        # criando o novo objeto pizza
        new_pizza = Pizza.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            creator=request.user,
        )
        return JsonResponse(data={
            'id': new_pizza.id,
            'title': new_pizza.title,
            'description': new_pizza.description
        })
    elif request.method == 'GET':
        try:
            pizza = Pizza.objects.get(id=p_id)
        except Pizza.DoesNotExist:
            return JsonResponse(data={
                'status': 'error',
                'msg': 'Objeto não encontrado',
            })
        return JsonResponse(data={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        })
    elif request.method == 'DELETE':
        if 'can_delete' in request.user.user_permissions:
            try:
                pizza = Pizza.objects.get(id=p_id)
                pizza.delete()
                return JsonResponse(data={
                    'status': 'error',
                    'msg': 'Pizza excluída'
                })
            except Pizza.DoesNotExist:
                return JsonResponse(data={
                    'status': 'error',
                    'msg': 'Pizza não existe',
                })
        else:
            return JsonResponse(data={
                'status': 'error',
                'msg': 'Não há permissão'
            })


@login_required
def random(request) -> JsonResponse:
    """Define a interface de acesso a um objeto aleatório.

    Args:
        request: Requisição padrão Django.

    Returns: Resposta Http.
    """
    # obtendo objeto aleatório
    try:
        pizza = Pizza.objects.all().order_by('?')[0]
        return JsonResponse(data={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        })
    except IndexError:
        return JsonResponse(data={
            'status': 'error',
            'msg': 'Objeto não encontrado',
        })


@login_required
def like(request) -> JsonResponse:
    """ Permite que um usuário curta uma determinada pizza.

    Args:
        request: Request padrão django.

    Returns: Resposta Http.
    """
    # somente aceitaremos requisições post
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            pizza = Pizza.objects.get(id=data.get('pizza'))
            new_like = Likes.objects.create(user=request.user,
                                            pizza=pizza,
                                            is_dislike=data.get('is_dislike',
                                                                False))
            return JsonResponse(data={
                'user': new_like.user,
                'pizza': new_like.pizza,
                'is_dislike': new_like.is_dislike
            })
        except Pizza.DoesNotExist:
            return JsonResponse(data={
                'status': 'error',
                'description': 'Pizza não existe no sistema.'
            })


class GetTenPizzasView(View):
    """View para obter 10 pizzas.
    """

    template_name = 'ten_pizzas.html'

    def get(self, request):
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})
