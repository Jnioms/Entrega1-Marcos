from django.urls import path
from taximetros.views import *

urlpatterns = [
    path("", index, name='taximetros_index'),
    path("crear/", crear, name='taximetros_crear')
]