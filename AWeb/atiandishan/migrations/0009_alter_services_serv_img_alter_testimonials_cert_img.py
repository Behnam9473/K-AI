# Generated by Django 4.2.5 on 2023-11-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atiandishan', '0008_alter_overview_cer_qty_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='serv_img',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='cert_img',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
