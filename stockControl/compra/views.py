from django.shortcuts import render
from .models import Producto, Proveedor
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def home(request):
    productosListados = Producto.objects.all()
    proveedoresListados = Proveedor.objects.all()
    return render(request, 'home.html', {"productos": productosListados, "proveedores": proveedoresListados})


def crearProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        precio = request.POST.get('numPrecio')
        stock_actual = request.POST.get('numStock')
        proveedor_id = request.POST.get('Proveedor')

        try:
            proveedor = Proveedor.objects.get(id=proveedor_id)
            print("Proveedor ID:", proveedor_id)

            producto = Producto.objects.create(nombre=nombre, precio=precio, stock_actual=stock_actual,
                                               proveedor=proveedor)
            return redirect('home')  # O redirige a otra vista si es necesario
        except Proveedor.DoesNotExist:
            return HttpResponse("Error: Proveedor no encontrado")

    elif request.method == 'GET':
        proveedores = Proveedor.objects.all()
        return render(request, 'agregarProducto.html', {'proveedores': proveedores})

def crearProveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        apellido = request.POST.get('txtApellido')
        dni = request.POST.get('numDni')

        try:
            proveedor = Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)
            return redirect('home')  # O redirige a otra vista si es necesario
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    elif request.method == 'GET':
        return render(request, 'agregarProveedor.html')
