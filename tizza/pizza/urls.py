from django.urls import path

from .views import index, random


urlpatterns = [
    path('<int:p_id>', index, name='pizza'),
    path('random', random, name='random'),
]
