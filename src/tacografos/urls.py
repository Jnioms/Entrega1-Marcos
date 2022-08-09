from django.urls import path
from tacografos.views import *

urlpatterns = [
    path("", index, name='tacografos_index'),
    path("crear/", crear, name='tacografos_crear')
]