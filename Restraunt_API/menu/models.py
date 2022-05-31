from django.db import models

# Create your models here.
class Menu(models.Model):
    Item_name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="menu/images", default="")
    Category = models.CharField(max_length=50)
    Price = models.FloatField()
    Discount = models.FloatField()
    Plate_size = models.IntegerField()

    def __str__(self):
        return self.Item_name