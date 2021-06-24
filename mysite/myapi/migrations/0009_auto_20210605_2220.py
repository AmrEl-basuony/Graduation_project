# Generated by Django 3.1 on 2021-06-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_auto_20210528_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='age_preference',
        ),
        migrations.RemoveField(
            model_name='application',
            name='image',
        ),
        migrations.RemoveField(
            model_name='application',
            name='salary_range',
        ),
        migrations.AddField(
            model_name='application',
            name='age_preference_high',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='age_preference_low',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='salary_range_high',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='salary_range_low',
            field=models.IntegerField(null=True),
        ),
    ]