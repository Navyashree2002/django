# Generated by Django 4.2.5 on 2023-11-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
