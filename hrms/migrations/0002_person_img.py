# Generated by Django 2.2.3 on 2020-10-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
