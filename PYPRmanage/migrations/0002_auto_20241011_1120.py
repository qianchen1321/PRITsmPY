# Generated by Django 3.0.2 on 2024-10-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PYPRmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_orders',
            name='Power',
            field=models.IntegerField(null=True),
        ),
    ]
