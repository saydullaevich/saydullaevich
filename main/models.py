from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    rasm = models.ImageField(verbose_name="Rasm")
    
