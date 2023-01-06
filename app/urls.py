from django.urls import path
from .views import home, base, agregar_guardia,listar_guardia,modificar_guardia,eliminar_guardia
from .views import agregar_empresa,listar_empresa, modificar_empresa

urlpatterns = [
    path('',home, name="home" ),
    path('base/',base, name="base" ),
    path('agregar-guardia/',agregar_guardia, name="agregar_guardia" ),
    path('listar-guardia/',listar_guardia, name="listar_guardia" ),
    path('modificar-guardia/<id>/',modificar_guardia, name="modificar_guardia" ),
    path('eliminar-guardia/<id>/',eliminar_guardia, name="eliminar_guardia" ),
    path('agregar-empresa/',agregar_empresa, name="agregar_empresa" ),
    path('listar-empresa/',listar_empresa, name="listar_empresa" ),
    path('modificar-empresa/<id>/',modificar_empresa, name="modificar_empresa" ),
   

    
]