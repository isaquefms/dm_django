from django.urls import path

from tizza.payments.views import index

urlpatterns = [
    path('', index, name='index')
]
