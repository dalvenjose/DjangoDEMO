# Generated by Django 5.1.2 on 2024-11-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0002_fruits'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=10)),
                ('marks', models.IntegerField(max_length=10)),
            ],
        ),
    ]