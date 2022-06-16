from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Product
# Create your views here.
def index (request):
    inventario_total = Product.objects.all()
    contexto = {'inventario':inventario_total}
    return render(request, 'index.html', contexto)

def venta (request, product_id):
    prod = Product.objects.filter(idem = product_id)
    contexto = {'producto':prod}
    return render(request, 'venta.html', contexto)
    