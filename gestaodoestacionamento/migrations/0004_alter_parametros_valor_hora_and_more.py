# Generated by Django 4.1 on 2023-01-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaodoestacionamento', '0003_parametros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='valor_hora',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='valor_mes',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
