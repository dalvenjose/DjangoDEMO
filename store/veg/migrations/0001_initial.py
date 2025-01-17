# Generated by Django 5.1.2 on 2024-10-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_number', models.IntegerField(max_length=10, unique=True)),
                ('customer_address', models.TextField(max_length=400)),
                ('order_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
