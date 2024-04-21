from django.db import models


class Product(models.Model):
    name =models.CharField(max_length=256)
    image = models.ImageField()
    price = models.FloatField()
    description = models.TextField()
    rate = models.IntegerField(default=0)
    category = models.CharField(max_length=23)



class ProdoctComents(models.Model):
    name = models.CharField(max_length=115)
    email = models.EmailField()
    review = models.TextField()
    rate = models.IntegerField(default=0)


class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
