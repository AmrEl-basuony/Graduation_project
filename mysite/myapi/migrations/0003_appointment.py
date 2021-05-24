# Generated by Django 3.1 on 2021-05-24 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_questiongrade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('availability', models.BooleanField(choices=[(True, 'Available'), (False, 'Not available')], default=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.employee')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.organization')),
            ],
        ),
    ]
