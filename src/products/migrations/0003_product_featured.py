# Generated by Django 2.1.5 on 2020-03-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200313_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
