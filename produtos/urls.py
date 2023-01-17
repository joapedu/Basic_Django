from django.urls import path
from . import views

urlpatterns = [
    path('ver/', views.ver_produto, name="ver_produto"),
    #http:www.|||.com/produtos/ver/
    path('inserir/', views.inserir_produto, name="inserir_produto"),
    #http:www.|||.com/produtos/inserir/
    path('ola/', views.ola_produto, name="ola_produto")
    #http:www.|||.com/produtos/ola/

    #endereço, linkView.Função, atribuir nome
]