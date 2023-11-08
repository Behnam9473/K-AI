# Generated by Django 4.2.5 on 2023-11-07 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atiandishan', '0003_alter_services_options_remove_services_serv_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_qty', models.IntegerField()),
                ('customer_qty_description', models.TextField(max_length=150)),
                ('project_qty', models.IntegerField()),
                ('project_qty_description', models.TextField(max_length=150)),
                ('expr_year', models.IntegerField()),
                ('expr_year_description', models.TextField(max_length=150)),
                ('cer_qty', models.IntegerField()),
                ('cer_qty_description', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'در یک نگاه',
                'verbose_name_plural': 'در یک نگاه',
            },
        ),
        migrations.AddField(
            model_name='about_us',
            name='about_long_description',
            field=models.TextField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about_us',
            name='about',
            field=models.TextField(max_length=150),
        ),
    ]