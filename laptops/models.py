from django.db import models

# Create your models here.

class Laptop(models.Model):

    image = models.ImageField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=20, default='Apple Macbook')
    year = models.IntegerField()
    screen_size = models.IntegerField()
    hard_drive_size = models.CharField(max_length=20)
    ram_size = models.CharField(max_length=20)
    processor_speed = models.CharField(max_length=20)
    delivery_option = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    instock = models.BooleanField()
    stock_size = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
