# Generated by Django 3.0.6 on 2021-04-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('middle_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
            ],
        ),
    ]