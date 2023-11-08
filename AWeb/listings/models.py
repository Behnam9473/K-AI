from django.db import models

# Create your models here.

type_choices =[('penu',"پنوماتیکی"),
                ("hydro","هیدرولیکی"),
                ("valves","شیرآلات صنعتی"),
            ]

class part(models.Model):
    part_name = models.CharField(max_length=50,)
    part_disctiption = models.TextField(max_length=200)
    part_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)
    part_customer = models.CharField(max_length=100,)
    part_type = models.CharField(choices = type_choices,)
    def __str__(self):
        return self.part_name
    class Meta:
        verbose_name = 'قطعات'
        verbose_name_plural = 'قطعات'