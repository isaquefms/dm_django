from django.urls import path

from .views import SingupView


urlpatterns = [
    path('register', SingupView.as_view())
]
