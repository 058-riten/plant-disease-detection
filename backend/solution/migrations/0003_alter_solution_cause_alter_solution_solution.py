# Generated by Django 5.0.3 on 2024-03-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0002_solution_cause'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='cause',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='solution',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
    ]
