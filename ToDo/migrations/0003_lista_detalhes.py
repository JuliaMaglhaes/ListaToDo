# Generated by Django 3.0.5 on 2020-09-14 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_auto_20200914_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='detalhes',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
