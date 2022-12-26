# Generated by Django 4.0.6 on 2022-08-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Winery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('specialty', models.CharField(max_length=40)),
                ('owner_name', models.CharField(max_length=40)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
