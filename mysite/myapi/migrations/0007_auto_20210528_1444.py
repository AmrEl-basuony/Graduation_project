# Generated by Django 3.1 on 2021-05-28 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20210528_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='myapi.employee', to_field='email'),
        ),
    ]
