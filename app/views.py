from django.shortcuts import render
from django.contrib import messages
from .forms import GuardiaForm,CustomUserCreationForm, EmpresaForm
from .models import Guardias, Empresa
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,'app/home.html')



def base(request):
    return render(request,'app/base.html')

@permission_required('app.add_guardias')
def agregar_guardia(request):
    
    data ={
        'form': GuardiaForm
        
    }
    if request.method == 'POST':
        formulario = GuardiaForm(data=request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardia agregado correctamente"
        else:
            data["form"] = formulario
    return render(request,'app/guard/agregar.html',data)

@permission_required('app.view_guardias')
def listar_guardia(request):
    guardia = Guardias.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(guardia,2)
        guardia = paginator.page(page)
    except:
        raise Http404
    
    
    data={
        
        'entity': guardia ,
        'paginator': paginator
    }
    return render(request, 'app/guard/listar.html',data)

@permission_required('app.change_guardias')
def modificar_guardia(request, id):
    guard = get_object_or_404(Guardias, id=id)
    print('guard')
    data ={
        'form' : GuardiaForm(instance=guard)
    }
    if request.method == 'POST':
        formulario = GuardiaForm(data=request.POST,instance=guard, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar_guardia")
        data["form"] = formulario
           
    return render(request,'app/guard/modificar.html',data)

@permission_required('app.delete_guardias')
def eliminar_guardia(request,id):
    guard = get_object_or_404(Guardias,id=id)
    guard.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="listar_guardia")


@permission_required('app.add_empresa')
def agregar_empresa(request):
    
    data ={
        'form': EmpresaForm
        
    }
    if request.method == 'POST':
        formulario = EmpresaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Empresa agregada correctamente"
        else:
            data["form"] = formulario
    return render(request,'app/empresa/agregar_empresa.html',data)

@permission_required('app.view_empresa')
def listar_empresa(request):
    empresa = Empresa.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(empresa,2)
        empresa = paginator.page(page)
    except:
        raise Http404
    
    
    data={
        
        'entity': empresa ,
        'paginator': paginator
    }
    return render(request, 'app/empresa/listar_empresa.html',data)


@permission_required('app.change_empresa')
def modificar_empresa(request, id):
    empre = get_object_or_404(Empresa, id=id)
    print('empre')
    data ={
        'form' : EmpresaForm(instance=empre)
    }
    if request.method == 'POST':
        formulario = EmpresaForm(data=request.POST,instance=empre, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar_empresa")
        data["form"] = formulario
           
    return render(request,'app/empresa/modificar_empresa.html',data)

