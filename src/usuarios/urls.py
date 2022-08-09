from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("", index, name='usuario_index'),
    path("crear/", crear, name='usuario_crear')
]