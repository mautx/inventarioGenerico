from operator import imod
from django.urls import path
from . import views

app_name = 'inputDatos'
urlpatterns = [
    path("", views.index, name = "principal_input"),
    path('<int:product_id>/', views.venta, name='venta'),
]