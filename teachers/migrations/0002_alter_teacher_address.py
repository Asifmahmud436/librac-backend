# Generated by Django 5.1.1 on 2024-09-27 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]