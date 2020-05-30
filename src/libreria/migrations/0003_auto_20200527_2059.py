# Generated by Django 3.0.5 on 2020-05-27 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_auto_20200527_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='sale',
            field=models.CharField(blank=True, choices=[('C', '5%'), ('D', '10%'), ('Q', '15%'), ('V', '20%')], max_length=1, null=True),
        ),
    ]