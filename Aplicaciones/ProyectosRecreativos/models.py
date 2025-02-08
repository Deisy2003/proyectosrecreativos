from django.db import models

# Create your models here.


class Cliente(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"


class Contratista(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='contratista/', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.empresa} "


class ParqueRecreativo(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)  # Área en metros cuadrados
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class ProyectoConstruccion(models.Model):
    parque = models.ForeignKey(ParqueRecreativo, on_delete=models.CASCADE)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(
        max_length=50, 
        choices=[("En Planificación", "En Planificación"), 
                 ("En Construcción", "En Construcción"), 
                 ("Finalizado", "Finalizado")]
    )

    def __str__(self):
        return f"Proyecto {self.parque.nombre} - {self.estado}"
    


