from django.shortcuts import render
from django.http import HttpResponse

def ver_produto(request):
    return HttpResponse('Estou no ver')

def inserir_produto(request):
    return HttpResponse('Estou no inserir')