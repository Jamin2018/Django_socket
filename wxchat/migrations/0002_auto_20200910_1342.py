# Generated by Django 3.0.3 on 2020-09-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxchat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isonline',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='socketid',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
