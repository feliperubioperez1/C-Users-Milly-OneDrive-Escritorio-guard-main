from django.contrib import admin
from .models import Guardias, Empresa

class GuardiasAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","apellido","rut","activo","foto","empresas"]
    list_editable = ["nombre","apellido","rut","activo","empresas"]
    search_fields = ["nombre"]
    list_filter = ["activo","empresas"]
    list_per_page = 5

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nombre","rut","activo"]
    list_filter = ["activo"]
    list_per_page = 10

# Register your models here.
admin.site.register(Guardias,GuardiasAdmin)
admin.site.register(Empresa,EmpresaAdmin)
    