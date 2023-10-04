# Generated by Django 4.2.5 on 2023-10-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
    ]