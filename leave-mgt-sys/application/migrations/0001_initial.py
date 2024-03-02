# Generated by Django 5.0.2 on 2024-02-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=10)),
            ],
        ),
    ]
