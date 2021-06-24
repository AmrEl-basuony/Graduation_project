# Generated by Django 3.1 on 2021-05-28 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20210528_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='myapi.organization', to_field='email'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='myapi.application'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='myapi.employee'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='myapi.organization'),
        ),
        migrations.AlterField(
            model_name='education',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='myapi.application'),
        ),
        migrations.AlterField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='myapi.employee', to_field='email'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='myapi.employee', to_field='email'),
        ),
        migrations.AlterField(
            model_name='professionalskill',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professionalskills', to='myapi.application'),
        ),
        migrations.AlterField(
            model_name='professionalskill',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professionsalskills', to='myapi.employee', to_field='email'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='myapi.test'),
        ),
        migrations.AlterField(
            model_name='questiongrade',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questiongrades', to='myapi.employee'),
        ),
        migrations.AlterField(
            model_name='questiongrade',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questiongrades', to='myapi.question'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socialLinks', to='myapi.organization', to_field='email'),
        ),
        migrations.AlterField(
            model_name='test',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='myapi.application'),
        ),
        migrations.AlterField(
            model_name='test',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='myapi.organization', to_field='email'),
        ),
    ]
