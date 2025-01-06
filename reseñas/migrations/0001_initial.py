# Generated by Django 4.2.11 on 2025-01-06 00:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservas', '0001_initial'),
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_el', models.DateTimeField(default=datetime.datetime.now)),
                ('clasificación', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('texto', models.TextField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas', to=settings.AUTH_USER_MODEL)),
                ('fecha_de_la_sesión', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reserva', to='reservas.reserva')),
                ('servicio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reseñas', to='services.services')),
            ],
            options={
                'ordering': ['-creado_el'],
            },
        ),
    ]
