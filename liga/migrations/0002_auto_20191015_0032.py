# Generated by Django 2.2.6 on 2019-10-15 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='logo',
            field=models.ImageField(default='media/federacion/liga/default.png', upload_to='media/federacion/liga/'),
        ),
    ]
