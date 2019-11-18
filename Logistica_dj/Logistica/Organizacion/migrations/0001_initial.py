# Generated by Django 2.2.6 on 2019-11-16 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_organizacion.punto_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Punto',
                'verbose_name_plural': 'Puntos',
            },
        ),
        migrations.CreateModel(
            name='PuntoDeRecepcion',
            fields=[
                ('punto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Organizacion.Punto')),
                ('tipo_de_establecimiento', models.CharField(choices=[('Casa Compañero', 'Casa Compañero'), ('Centro Barrial', 'Centro Barrial'), ('Comendor', 'Comedor'), ('Cooperativa', 'Cooperativa'), ('Merendero-Comedor', 'Merendero-Comedor')], default='', max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=80)),
                ('localidad', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('observacion', models.TextField(blank=True)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Punto de Recepción',
                'verbose_name_plural': 'Punto de Recepción',
            },
            bases=('Organizacion.punto',),
        ),
        migrations.CreateModel(
            name='PuntoDeConsumo',
            fields=[
                ('punto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Organizacion.Punto')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=80)),
                ('localidad', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('tipo_de_establecimiento', models.CharField(choices=[('Casa Comunitaria', 'Casa Comunitaria'), ('Centro Barrial', 'Centro Barrial'), ('Comendor', 'Comedor'), ('Cooperativa', 'Cooperativa'), ('Merendero', 'Merendero'), ('Merendero-Comedor', 'Merendero-Comedor')], default='', max_length=20)),
                ('observacion', models.TextField(blank=True)),
                ('punto_de_recepcion', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Organizacion.PuntoDeRecepcion')),
            ],
            options={
                'verbose_name': 'Punto de Consumo',
                'verbose_name_plural': 'Punto de Consumo',
            },
            bases=('Organizacion.punto',),
        ),
    ]