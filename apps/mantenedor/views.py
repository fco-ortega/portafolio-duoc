from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Cliente, Proveedor, Plato, Orden_compra, Empleado, Orden_pedido, Producto, Reporte, Huesped, Habitacion
from .forms import UsuarioCreationForm, UsuarioChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

#Usuario
class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/usuario_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UsuarioCreationForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UsuarioChangeForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

#Cliente
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ('rut_cliente', 'nombre', 'giro', 'direccion', 'id_usuario')
    success_url = reverse_lazy('cliente_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ('rut_cliente', 'nombre', 'giro', 'direccion', 'id_usuario')
    success_url = reverse_lazy('cliente_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

#Proveedor

class ProveedorList(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedores/proveedor_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ProveedorCreate(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = 'proveedores/proveedor_form.html'
    fields = ('rut_proveedor', 'nombre', 'giro', 'direccion', 'numero', 'id_usuario')
    success_url = reverse_lazy('proveedor_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ProveedorUpdate(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = 'proveedores/proveedor_form.html'
    fields = ('rut_proveedor', 'nombre', 'giro', 'direccion', 'numero', 'id_usuario')
    success_url = reverse_lazy('proveedor_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ProveedorDelete(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

#Platos

class PlatoList(LoginRequiredMixin, ListView):
    model = Plato
    template_name = 'comedor/plato_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class PlatoCreate(LoginRequiredMixin, CreateView):
    model = Plato
    template_name = 'comedor/plato_form.html'
    fields = ('id', 'nombre', 'precio', 'tipo')
    success_url = reverse_lazy('plato_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class PlatoUpdate(LoginRequiredMixin, UpdateView):
    model = Plato
    template_name = 'comedor/plato_form.html'
    fields = ('id', 'nombre', 'precio', 'tipo')
    success_url = reverse_lazy('plato_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class PlatoDelete(LoginRequiredMixin, DeleteView):
    model = Plato
    template_name = 'comedor/plato_confirm_delete.html'
    success_url = reverse_lazy('plato_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

#Orden de compra
class OrdenCompraList(LoginRequiredMixin, ListView):
    model = Orden_compra
    template_name = 'oc/oc_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class OrdenCompraCreate(LoginRequiredMixin, CreateView):
    model = Orden_compra
    template_name = 'oc/oc_form.html'
    fields = ('numero_orden', 'nombre_orden', 'fecha', 'fecha_entrega', 'rut_cliente')
    success_url = reverse_lazy('oc_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class OrdenCompraUpdate(LoginRequiredMixin, UpdateView):
    model = Orden_compra
    template_name = 'oc/oc_form.html'
    fields = ('numero_orden', 'nombre_orden', 'fecha', 'fecha_entrega', 'estado', 'rut_cliente')
    success_url = reverse_lazy('oc_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class OrdenCompraDelete(LoginRequiredMixin, DeleteView):
    model = Orden_compra
    template_name = 'oc/oc_confirm_delete.html'
    success_url = reverse_lazy('oc_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class OrdenCompraCancel(LoginRequiredMixin, UpdateView):
    model = Orden_compra
    template_name = 'oc/oc_form.html'
    fields = ('estado',)
    success_url = reverse_lazy('oc_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

# Producto

class ProductoList(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ('id_producto', 'nombre', 'cantidad', 'tipo', 'stock_critico', 'stock', 'descripcion', 'precio', 'id_orden_pedido')
    success_url = reverse_lazy('producto_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ('id_producto', 'nombre', 'cantidad', 'tipo', 'stock_critico', 'stock', 'descripcion', 'precio', 'id_orden_pedido')
    success_url = reverse_lazy('producto_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

#Empleado
class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ('run_empleado', 'nombres', 'apellidos', 'genero', 'telefono_movil', 'id_usuario')
    success_url = reverse_lazy('empleado_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ('run_empleado', 'nombres', 'apellidos', 'genero', 'telefono_movil', 'id_usuario')
    success_url = reverse_lazy('empleado_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

#Orden_pedido

class Orden_pedidoList(LoginRequiredMixin, ListView):
    model = Orden_pedido
    template_name = 'orden_pedidos/orden_pedido_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class Orden_pedidoCreate(LoginRequiredMixin, CreateView):
    model = Orden_pedido
    template_name = 'orden_pedidos/orden_pedido_form.html'
    fields = ('id_orden_pedido', 'fecha_emision', 'fecha_despacho', 'fecha_recepcion', 'estado', 'rut_proveedor')
    success_url = reverse_lazy('orden_pedido_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class Orden_pedidoUpdate(LoginRequiredMixin, UpdateView):
    model = Orden_pedido
    template_name = 'orden_pedidos/orden_pedido_form.html'
    fields = ('id_orden_pedido', 'fecha_emision', 'fecha_despacho', 'fecha_recepcion', 'estado', 'rut_proveedor')
    success_url = reverse_lazy('orden_pedido_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class Orden_pedidoDelete(LoginRequiredMixin, DeleteView):
    model = Orden_pedido
    template_name = 'orden_pedidos/orden_pedido_confirm_delete.html'
    success_url = reverse_lazy('orden_pedido_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ReporteList(LoginRequiredMixin, ListView):
    model = Reporte
    template_name = 'reportes/reporte_list.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ReporteCreate(LoginRequiredMixin, CreateView):
    model = Reporte
    template_name = 'reportes/reporte_form.html'
    fields = ('id_reporte', 'nombre', 'fecha')
    success_url = reverse_lazy('reporte_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ReporteUpdate(LoginRequiredMixin, UpdateView):
    model = Reporte
    template_name = 'reportes/reporte_form.html'
    fields = ('id_reporte', 'nombre')
    success_url = reverse_lazy('reporte_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

class ReporteDelete(LoginRequiredMixin, DeleteView):
    model = Reporte
    template_name = 'reportes/reporte_confirm_delete.html'
    success_url = reverse_lazy('reporte_list')
    login_url = '/'
    redirect_field_name = 'redirect_to'

#Huesped

class HuespedList(ListView):
    model = Huesped
    template_name = 'huesped/huesped_list.html'

class HuespedCreate(CreateView):
    model = Huesped
    template_name = 'huesped/huesped_form.html'
    fields = ('run_huesped', 'nombres', 'apellidos', 'genero', 'telefono_movil')
    success_url = reverse_lazy('huesped_list')

class HuespedUpdate(UpdateView):
    model = Huesped
    template_name = 'huesped/huesped_form.html'
    fields = ('run_huesped', 'nombres', 'apellidos', 'genero', 'telefono_movil')
    success_url = reverse_lazy('huesped_list')

class HuespedDelete(DeleteView):
    model = Huesped
    template_name = 'huesped/huesped_confirm_delete.html'
    success_url = reverse_lazy('huesped_list')

#Habitacion

class HabitacionList(ListView):
    model = Habitacion
    template_name = 'habitacion/habitacion_list.html'

class HabitacionCreate(CreateView):
    model = Habitacion
    template_name = 'habitacion/habitacion_form.html'
    fields = ('id_habitacion', 'tipo_cama', 'accesorios', 'precio')
    success_url = reverse_lazy('habitacion_list')

class HabitacionUpdate(UpdateView):
    model = Habitacion
    template_name = 'habitacion/habitacion_form.html'
    fields = ('id_habitacion', 'tipo_cama', 'accesorios', 'precio')
    success_url = reverse_lazy('habitacion_list')

class HabitacionDelete(DeleteView):
    model = Habitacion
    template_name = 'habitacion/habitacion_confirm_delete.html'
    success_url = reverse_lazy('habitacion_list')


# Manual de ayuda
def manual_ayuda(request):
    return render(request, 'manual.html')
