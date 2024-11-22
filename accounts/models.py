from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# # Create your models here.
# class UsuarioC(AbstractUser):
#     ROLES = (
#         ('cliente', 'Cliente'),
#         ('admin', 'Admin'),
#         ('moderador', 'Moderador'),
#         ('otro', 'Otro'),
#     )

#     rol = models.CharField(max_length=10, choices=ROLES, default='cliente')

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_problema = models.CharField(max_length=100, verbose_name='Problema')
    ticket_detalles = models.TextField(max_length=1000, verbose_name='Detalles')
    PRIORIDAD_OPCIONES = [(1,'Baja'),(2,'Media'),(3,'Alta')]
    ticket_prioridad = models.IntegerField(choices=PRIORIDAD_OPCIONES,  default='baja',verbose_name='Prioridad')
    ESTADO_OPCIONES = [('abierto','Abierto'),('enproceso','En proceso'),('resuelto','Resuelto'),('cerrado','Cerrado')]
    ticket_estado = models.CharField(max_length=20,choices=ESTADO_OPCIONES, default='abierto',verbose_name='estado')
    ticket_tecnico_responsable = models.CharField(max_length = 150,default='',blank=True, verbose_name='Tecnico Responsable')
    ticket_fecha_creacion = models.DateTimeField(default=now,editable=False, blank=True, verbose_name='Fecha agregado')
