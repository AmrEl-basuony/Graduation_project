# Generated by Django 3.1 on 2021-05-26 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='application',
            name='job_requirements',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.application'),
        ),
        migrations.AddField(
            model_name='questiongrade',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.test'),
        ),
        migrations.AddField(
            model_name='test',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.application'),
        ),
    ]
