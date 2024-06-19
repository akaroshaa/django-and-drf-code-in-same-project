from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    doj = models.DateField()
    salary = models.FloatField(default=0)

    def __str__(self):
        return self.name
