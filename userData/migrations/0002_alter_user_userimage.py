# Generated by Django 5.0.6 on 2024-05-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userImage',
            field=models.ImageField(upload_to='userphotos/%y%m%d'),
        ),
    ]
