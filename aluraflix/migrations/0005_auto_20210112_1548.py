# Generated by Django 3.1.5 on 2021-01-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0004_auto_20210112_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='tipo',
            field=models.CharField(choices=[('F', 'Filme'), ('S', 'Serie')], default=True, max_length=1),
        ),
    ]
