# Generated by Django 3.1.1 on 2020-09-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=50)),
            ],
        ),
    ]