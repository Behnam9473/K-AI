from django.db import models

# Create your models here.

type_choices =[('penu',"پنوماتیکی"),
                ("hydro","هیدرولیکی"),
                ("valves","شیرآلات صنعتی"),
            ]

class metering_valve (models.Model):
    part_name = models.CharField(max_length=100,)
    general_part_discription = models.TextField(max_length=1800)
    part_image_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_a = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_b = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_c = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_d = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_customer = models.CharField(max_length=150,)
    part_type = models.CharField(max_length=100, choices = type_choices,)
    #part_catalog = models.FileField( upload_to='documents/%Y/%m/%d/', )
    part_exact_discription = models.TextField(max_length=800)


    def __str__(self):
        return self.part_name
    class Meta:
        verbose_name = 'مقسم گریس'
        verbose_name_plural = 'مقسم گریس'


class air_impact(models.Model):
    part_name = models.CharField(max_length=100,)
    general_part_discription = models.TextField(max_length=1800)
    part_image_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_a = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_b = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_c = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_image_d = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False,)
    part_customer = models.CharField(max_length=150,)
    part_type = models.CharField(max_length=100, choices = type_choices,)
    #part_catalog = models.FileField( upload_to='documents/%Y/%m/%d/', )
    part_exact_discription = models.TextField(max_length=800)
    part_model = models.CharField(max_length=150,)
    part_drive_type = models.CharField(max_length=150,)
    part_drive_size = models.CharField(max_length=150,)
    part_type_air_impact = models.CharField(max_length=150,)
    part_torque = models.CharField(max_length=150,)
    part_BPM = models.CharField(max_length=150,)
    part_sound_level = models.CharField(max_length=150,)
    part_vibration_level = models.CharField(max_length=150,)
    part_weight = models.CharField(max_length=150,)
    part_dim = models.CharField(max_length=150,)
    part_air_inlet = models.CharField(max_length=150,)
    part_min_hose_size = models.CharField(max_length=150,)
    part_average_air_consumption  = models.CharField(max_length=150,)
    def __str__(self):
        return self.part_name
    class Meta:
        verbose_name = 'بکس بادی'
        verbose_name_plural = 'بکس بادی'