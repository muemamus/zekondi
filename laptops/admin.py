from django.contrib import admin
from .models import Laptop

class LaptopAdmin(admin.ModelAdmin):

    list_display = (
         "image",
         "name",
          "year",
          "screen_size",
          "image_url",
          "hard_drive_size",
          "ram_size",
          "processor_speed",
          "delivery_option",
          "price",
          "instock",
          "stock_size"
    )
# Register your models here.
admin.site.register(Laptop,LaptopAdmin)

