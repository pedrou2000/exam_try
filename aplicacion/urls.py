from django.urls import path
from .views import usuarios_1002
urlpatterns = [
    path('usuario/', usuarios_1002, name='usuario'),
]