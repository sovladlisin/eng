# Generated by Django 3.0.3 on 2020-02-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200214_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('icon', models.CharField(max_length=300)),
                ('text', models.TextField()),
            ],
        ),
    ]