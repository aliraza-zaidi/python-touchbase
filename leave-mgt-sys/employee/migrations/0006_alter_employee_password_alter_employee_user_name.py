# Generated by Django 5.0.2 on 2024-02-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employee_password_employee_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(default='xyz', max_length=18),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_name',
            field=models.CharField(default='abcd', max_length=15),
        ),
    ]
