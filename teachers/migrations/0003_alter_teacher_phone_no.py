# Generated by Django 5.1.1 on 2024-09-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacher_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]