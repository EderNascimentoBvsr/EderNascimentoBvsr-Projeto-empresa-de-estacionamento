# Generated by Django 4.1 on 2023-01-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaodoestacionamento', '0006_alter_clienterotativo_valor_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienterotativo',
            name='valor_hora',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]