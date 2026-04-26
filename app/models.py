from django.db import models

# Create your models here.

class Alumno(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    estado = models.BooleanField()

    class Meta:
        db_table = "alumno"  # Especificar el nombre de la tabla que se creara en la migración

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
