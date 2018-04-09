from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings
import re


def validate_product_name(prodname):
    regex_string = r'^\w[\w ]*$'
    search = re.compile(regex_string).search
    result = bool(search(prodname))
    if not result:
        raise ValidationError("Please only use letters, "
                              "numbers and underscores or spaces. "
                              "The name cannot start with a space.")


'''class Product(models.Model):
    name = models.CharField(max_length=100,
                            validators=[validate_product_name])
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock_applies = models.BooleanField()
    stock = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def clean(self):
        validate_product_name(self.name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.full_clean()
        return super(Product, self).save(*args, **kwargs)'''


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      default=0)
    done = models.BooleanField(default=False)
    last_change = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('view_order', args=[self.id])


class Cash(models.Model):
    amount = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 default=0)

class Pizzas(models.Model):
    pizza_name = models.CharField(max_length=254, unique= True)
    def __str__ (self):
        return self.pizza_name
    category= models.CharField(max_length=254, unique= True)
    def __str__ (self):
        return self.pizza_name
    pizza_size = models.ForeignKey(Price)
class Order_Item(models.Model):
    pizza_name = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    pizza_size = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    name = models.CharField(Toppings, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class Setting(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.key

    def __bool__(self):
        return bool(self.value)

    __nonzero__ = __bool__


class Price(models.Model):
    pizza_size = models.CharField(max_length=254, unique= True)
    price = models.CharField(max_length=254)


class Toppings(models.Model):
    name = models.CharField(max_length= 75, unique=True)
    price = models.CharField(max_length=55)

    def __str__ (self):
        return self.name
