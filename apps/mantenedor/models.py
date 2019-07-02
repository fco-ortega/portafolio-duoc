from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=14, primary_key=True)
    nombre = models.CharField(max_length=30)
    giro = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    rut_proveedor = models.CharField(max_length=14, primary_key=True)
    nombre = models.CharField(max_length=30)
    giro = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    numero = models.CharField(max_length=13)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=30)

class Orden_compra(models.Model):
    ESTADO = (
        ('A', 'Activa'),
        ('C', 'Cancelada'),
    )
    numero_orden = models.IntegerField(primary_key=True)
    nombre_orden = models.CharField(max_length=50)
    fecha = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Empleado(models.Model):
    run_empleado = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    genero = models.CharField(max_length=1)
    telefono_movil = models.CharField(max_length=12)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Orden_pedido(models.Model):
    ESTADO = (
        ('A', 'Abierta'),
        ('E', 'Enviada'),
        ('R', 'Recibida'),
    )
    id_orden_pedido = models.IntegerField(primary_key=True)
    fecha_emision = models.DateField()
    fecha_despacho = models.DateField()
    fecha_recepcion = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')
    rut_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=50)
    stock_critico = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    id_orden_pedido = models.ForeignKey(Orden_pedido, on_delete=models.CASCADE)

class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)

class Habitacion(models.Model):
    id_habitacion = models.IntegerField(primary_key=True)
    tipo_cama = models.CharField(max_length=15)
    accesorios = models.CharField(max_length=50)
    precio = models.IntegerField()
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Huesped(models.Model):
    run_huesped = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    telefono_movil = models.CharField(max_length=15)
    correo = models.CharField(max_length=30)
    id_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Reporte(models.Model):
    id_reporte = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    fecha = models.DateField(default=datetime.date.today())

    def fecha_format(self):
        #OJO, LO ENTREGA MES-DIA-ANIO, GRINGO STYLE
        return str(self.fecha.month) + '/' + str(self.fecha.day) + '/' + str(self.fecha.year)

    def suma_mensual(self):
        mes = self.fecha.month
        anio = self.fecha.year
        #dates = Orden_compra.objects.get(numero_orden=2).fecha_entrega.month
        oc_generadas = Orden_compra.objects.filter(fecha_entrega__month=mes, fecha_entrega__year=anio)
        clientes = []
        suma = 0
        if oc_generadas.count() > 0:
            for oc in oc_generadas:
                for cl in Cliente.objects.all():
                    if oc.rut_cliente.rut_cliente == cl.rut_cliente:
                        clientes.append(cl.rut_cliente)

            if Huesped.objects.count() > 0 and len(clientes) > 0:
                for h in Huesped.objects.all():
                    for c in clientes:
                        if h.rut_cliente == c:
                            suma = suma + 72015

        return suma
