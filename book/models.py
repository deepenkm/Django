from django.db import models

# Create your models here.
def validate_price(price):
    if price<100 or price >1000:
        raise ValueError('Price must be between 100 and 1000')
    else:
        return price

class Book(models.Model):
    title = models.CharField(max_length=56, null=False, blank=False, unique=True, verbose_name = 'Book Title')
    author = models.CharField(max_length=56,null=False ,blank=False)
    price = models.IntegerField(validators = [validate_price] ,null=False)
    description = models.CharField(max_length=256, null=False ,verbose_name = 'Book Description')

    def __str__(self):
        return self.title
