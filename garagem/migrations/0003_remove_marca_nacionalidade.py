# Generated by Django 4.2.4 on 2023-08-17 01:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0002_alter_categoria_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marca",
            name="nacionalidade",
        ),
    ]
