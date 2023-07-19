from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    #stored_in = models.ForeignKey("warehouse.Warehouse", on_delete=models.CASCADE, related_name='items')
