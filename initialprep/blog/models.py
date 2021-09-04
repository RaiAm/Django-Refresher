from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    
    def __str__(self):
        return self.product_name
