# Generated by Django 3.0.2 on 2024-10-11 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_type', models.CharField(max_length=20)),
                ('Business_type', models.CharField(max_length=20)),
                ('Brand', models.CharField(max_length=10)),
                ('Device_config', models.CharField(max_length=500)),
                ('Quantity_require', models.IntegerField()),
                ('Power', models.IntegerField()),
            ],
        ),
    ]
