from django.db import models

class about_us(models.Model):
    about = models.TextField(max_length=150,)
    about_long_description = models.TextField(max_length=1500,)
    def __str__(self):
        return "درباره ما"
    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

class overview(models.Model):
    customer_qty = models.IntegerField()
    customer_qty_description = models.TextField(max_length=1500,)
    
    project_qty = models.IntegerField()
    project_qty_description = models.TextField(max_length=1500,)

    expr_year = models.IntegerField()
    expr_year_description = models.TextField(max_length=1500,)

    cer_qty = models.IntegerField()
    cer_qty_description = models.TextField(max_length=1500,)
    def __str__(self):
        return " دریک نگاه"
    class Meta:
        verbose_name = 'در یک نگاه'
        verbose_name_plural = 'در یک نگاه'




class Testimonials(models.Model):
    cert_img = models.ImageField(upload_to='photos/%Y/%m/%d/',)
    cert_name = models.CharField(max_length=50,)
    cert_description = models.TextField(max_length=1500,)
    def __str__(self):
        return self.cert_name
    class Meta:
        verbose_name = 'گواهی نامه ها'
        verbose_name_plural = 'تقدیرنامه'


class services(models.Model):
    serv_name = models.CharField(max_length=50,)
    #serv_description = models.TextField(max_length=1500)
    serv_img = models.ImageField(upload_to='photos/%Y/%m/%d/',)
    def __str__(self):
        return self.serv_name
    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'




# Create your models here.
