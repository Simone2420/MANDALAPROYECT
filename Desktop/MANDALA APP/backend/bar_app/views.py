from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ProductoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovimientoSerializer
from .serializers import ComandaSerializer
from .serializers import MesaSerializer
from .models import Movimiento
from rest_framework import status

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-id')
    serializer_class = ProductoSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all().order_by("-fecha")
    serializer_class = MovimientoSerializer

def perform_create(self, serializer):
        movimiento = serializer.save()
        producto = movimiento.producto

        if movimiento.tipo == "entrada":
            producto.stock += movimiento.cantidad
        elif movimiento.tipo == "salida":
            producto.stock -= movimiento.cantidad

        producto.save()

        return Response({
            "movimiento": MovimientoSerializer(movimiento).data,
            "producto": ProductoSerializer(producto).data
        }, status=status.HTTP_201_CREATED)

class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all().order_by('-fecha_hora')
    serializer_class = ComandaSerializer

    def perform_create(self, serializer):
        comanda = serializer.save()
        for item in ComandaProducto.objects.filter(comanda=comanda):
            producto = item.producto
            if producto.stock < item.cantidad:
                raise ValueError(f"❌ Stock insuficiente para el producto {producto.nombre}.")
            producto.stock -= item.cantidad
            producto.save()

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all().order_by('numero')
    serializer_class = MesaSerializer
    def perform_create(self, serializer):
        if Mesa.objects.filter(numero=serializer.validated_data['numero']).exists():
            raise ValueError("❌ Ya existe una mesa con ese número.")
        serializer.save()
    
@api_view(['GET'])
def productos_list(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

