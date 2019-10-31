# Generated by Django 2.2.6 on 2019-10-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('logo', models.ImageField(default='federacion/liga/default.png', upload_to='federacion/liga/')),
            ],
        ),
    ]