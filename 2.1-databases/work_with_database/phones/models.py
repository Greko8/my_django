from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, null=False, unique=True)
