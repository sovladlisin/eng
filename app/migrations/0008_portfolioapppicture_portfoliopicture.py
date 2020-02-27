# Generated by Django 3.0.3 on 2020-02-15 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_job_full_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioAppPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Не указано', max_length=150)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='app.PortfolioAppPicture/bytes/filename/mimetype')),
                ('portfolio_job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.PortfolioCard')),
            ],
        ),
    ]