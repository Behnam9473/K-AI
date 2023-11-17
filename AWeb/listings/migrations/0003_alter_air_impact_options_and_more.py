# Generated by Django 4.1.2 on 2023-11-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_air_impact_metering_valve_delete_part'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='air_impact',
            options={'verbose_name': 'بکس بادی', 'verbose_name_plural': 'بکس بادی'},
        ),
        migrations.AlterModelOptions(
            name='metering_valve',
            options={'verbose_name': 'مقسم گریس', 'verbose_name_plural': 'مقسم گریس'},
        ),
        migrations.AddField(
            model_name='air_impact',
            name='part_type_air_impact',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='air_impact',
            name='part_type',
            field=models.CharField(choices=[('penu', 'پنوماتیکی'), ('hydro', 'هیدرولیکی'), ('valves', 'شیرآلات صنعتی')], max_length=100),
        ),
    ]