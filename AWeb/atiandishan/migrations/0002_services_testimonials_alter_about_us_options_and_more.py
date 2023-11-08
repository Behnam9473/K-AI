# Generated by Django 4.2.5 on 2023-10-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atiandishan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_name', models.CharField(max_length=50)),
                ('serv_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_img', models.ImageField(upload_to='')),
                ('cert_name', models.CharField(max_length=50)),
                ('cert_description', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'گواهی نامه ها',
                'verbose_name_plural': 'تقدیرنامه',
            },
        ),
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name': 'درباره ما', 'verbose_name_plural': 'درباره ما'},
        ),
        migrations.AlterModelOptions(
            name='part',
            options={'verbose_name': 'قطعات', 'verbose_name_plural': 'قطعات'},
        ),
    ]
