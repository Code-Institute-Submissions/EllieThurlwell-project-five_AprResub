from django.db import models


class Category(models.Model):
    """ schema for category model """
    name = models.CharField(max_length=256)
    friendly_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ schema for products model """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
