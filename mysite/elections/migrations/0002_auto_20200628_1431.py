# Generated by Django 3.0.7 on 2020-06-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_number',
            field=models.IntegerField(default=0),
        ),
    ]