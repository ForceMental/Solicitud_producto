from django.shortcuts import render
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductoListView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
