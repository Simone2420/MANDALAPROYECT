from rest_framework import serializers
from .models import Producto, Movimiento, Comanda, Mesa, ComandaProducto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'
class ComandaProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)  # Para lectura
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), 
        write_only=True, 
        source='producto'
    )

    class Meta:
        model = ComandaProducto
        fields = ['producto', 'producto_id', 'cantidad']
class ComandaSerializer(serializers.ModelSerializer):
    productos = ComandaProductoSerializer(many=True, write_only=True)
    productos_detalle = ComandaProductoSerializer(source='comandaproducto_set', many=True, read_only=True)

    class Meta:
        model = Comanda
        fields = '__all__'

    def create(self, validated_data):
        productos_data = validated_data.pop('productos', [])
        comanda = Comanda.objects.create(**validated_data)
        total = 0
        for item in productos_data:
            producto = item['producto']  
            cantidad = item['cantidad']
            ComandaProducto.objects.create(comanda=comanda, producto=producto, cantidad=cantidad)
            total += producto.precio * cantidad
        comanda.total = total
        comanda.save()
        return comanda

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
    

