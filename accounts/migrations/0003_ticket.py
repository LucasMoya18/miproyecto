# Generated by Django 3.2 on 2024-11-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_delete_usuarioc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_problema', models.CharField(max_length=100, verbose_name='Problema')),
                ('ticket_detalles', models.CharField(max_length=200, verbose_name='Detalles')),
                ('ticket_prioridad', models.IntegerField(choices=[('Baja', 1), ('Media', 2), ('Alta', 3)], default='baja', verbose_name='')),
                ('ticket_estado', models.CharField(choices=[('abierto', 'Abierto'), ('enproceso', 'En proceso'), ('resuelto', 'Resuelto'), ('cerrado', 'Cerrado')], default='abierto', max_length=20, verbose_name='estado')),
                ('ticket_tecnico_responsable', models.CharField(max_length=150, verbose_name='Tecnico Responsable')),
                ('ticket_fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha agregado')),
            ],
        ),
    ]
