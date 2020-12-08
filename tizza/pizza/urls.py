from django.urls import path

from .views import index, random, like, GetTenPizzasView


urlpatterns = [
    path('<int:p_id>', index, name='pizza'),
    path('random', random, name='random'),
    path('like', like, name='like'),
    path('ten', GetTenPizzasView.as_view())
]
