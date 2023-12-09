from django.db import models

class News(models.Model):
    title = models.TextField(max_length=255,verbose_name="عنوان")
    body = models.TextField(max_length=1000, verbose_name="متن اصلی خبر")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="عکس خبر")
