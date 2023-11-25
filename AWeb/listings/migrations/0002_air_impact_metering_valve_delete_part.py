# Generated by Django 4.2.7 on 2023-11-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='air_impact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=100)),
                ('general_part_discription', models.TextField(max_length=1800)),
                ('part_image_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('part_image_a', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('part_image_b', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('part_customer', models.CharField(max_length=150)),
                ('part_type', models.CharField(choices=[('penu', 'پنوماتیکی'), ('hydro', 'هیدرولیکی'), ('valves', 'شیرآلات صنعتی')], max_length=100)),
                ('part_exact_discription', models.TextField(max_length=800)),
                ('part_model', models.CharField(max_length=150)),
                ('part_drive_type', models.CharField(max_length=150)),
                ('part_drive_size', models.CharField(max_length=150)),
                ('part_type_air_impact', models.CharField(max_length=150)),
                ('part_torque', models.CharField(max_length=150)),
                ('part_BPM', models.CharField(max_length=150)),
                ('part_sound_level', models.CharField(max_length=150)),
                ('part_vibration_level', models.CharField(max_length=150)),
                ('part_weight', models.CharField(max_length=150)),
                ('part_dim', models.CharField(max_length=150)),
                ('part_air_inlet', models.CharField(max_length=150)),
                ('part_min_hose_size', models.CharField(max_length=150)),
                ('part_average_air_consumption', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'بکس بادی',
                'verbose_name_plural': 'بکس بادی',
            },
        ),
        migrations.CreateModel(
            name='metering_valve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=100)),
                ('general_part_discription', models.TextField(max_length=1800)),
                ('part_image_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('part_image_a', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('part_customer', models.CharField(max_length=150)),
                ('part_type', models.CharField(choices=[('penu', 'پنوماتیکی'), ('hydro', 'هیدرولیکی'), ('valves', 'شیرآلات صنعتی')], max_length=100)),
                ('part_exact_discription', models.TextField(max_length=800)),
                ('part_temp', models.CharField(max_length=8)),
                ('part_perssure', models.CharField(max_length=8)),
                ('part_oprating_cycles', models.CharField(max_length=8)),
                ('part_min_viscosity', models.CharField(max_length=8)),
                ('part_greaes_max', models.CharField(max_length=15)),
                ('part_inlet_connection', models.CharField(max_length=15)),
                ('part_oulet_connection', models.CharField(max_length=15)),
                ('part_outlet_no', models.CharField(max_length=15)),
                ('part_max_volume', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'مقسم گریس',
                'verbose_name_plural': 'مقسم گریس',
            },
        ),
        migrations.DeleteModel(
            name='part',
        ),
    ]
