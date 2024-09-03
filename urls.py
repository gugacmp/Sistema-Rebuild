from django.urls import path
from .views import index, cadastrouser, validaruser, menu, rebuild

urlpatterns =[
    path('',index),
    path('cadastrouser', cadastrouser),
    path('validaruser', validaruser),
    path('menu', menu),
    path('rebuild', rebuild)
    
]