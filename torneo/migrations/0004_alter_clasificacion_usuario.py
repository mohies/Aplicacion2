# Generated by Django 5.1.2 on 2024-10-30 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0003_alter_clasificacion_usuario_alter_usuario_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacion',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='torneo.usuario'),
        ),
    ]
