from django.shortcuts import render
from django.http import HttpResponse

def ver_produto(request):
    return render(request, 'ver_produto.html')
    #http:www.|||.com/produtos/ver/

def inserir_produto(request):
    return render(request, 'inserir_produto.html')
    #http:www.|||.com/produtos/inserir/

def ola_produto(request):
    return render(request, 'ola_produto.html', {'nome': 'caio'})
    #http:www.|||.com/produtos/ola/
