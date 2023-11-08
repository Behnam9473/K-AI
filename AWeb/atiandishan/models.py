from django.db import models

class about_us(models.Model):
    about = models.TextField(max_length=150,)
    about_long_description = models.TextField(max_length=500,)
    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

class overview(models.Model):
    customer_qty = models.IntegerField()
    customer_qty_description = models.TextField(max_length=150,)
    
    project_qty = models.IntegerField()
    project_qty_description = models.TextField(max_length=150,)

    expr_year = models.IntegerField()
    expr_year_description = models.TextField(max_length=150,)

    cer_qty = models.IntegerField()
    cer_qty_description = models.TextField(max_length=150,)
    class Meta:
        verbose_name = 'در یک نگاه'
        verbose_name_plural = 'در یک نگاه'




class Testimonials(models.Model):
    cert_img = models.ImageField()
    cert_name = models.CharField(max_length=50,)
    cert_description = models.TextField(max_length=150,)
    class Meta:
        verbose_name = 'گواهی نامه ها'
        verbose_name_plural = 'تقدیرنامه'


class services(models.Model):
    serv_name = models.CharField(max_length=50,)
    serv_description = models.TextField(max_length=100)
    serv_img = models.ImageField()
    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'




# Create your models here.
