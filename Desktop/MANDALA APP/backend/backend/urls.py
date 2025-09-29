
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bar_app.views import ProductoViewSet
from bar_app import views
from bar_app.views import MovimientoViewSet
from bar_app.views import ComandaViewSet
from bar_app.views import MesaViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'movimientos', MovimientoViewSet, basename='movimiento')
router.register(r'comandas', ComandaViewSet, basename='comanda')
router.register(r'mesas', MesaViewSet, basename='mesa')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('productos/', views.productos_list),
    
]
