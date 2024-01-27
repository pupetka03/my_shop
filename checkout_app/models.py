from django.db import models
from django.contrib.auth.models import User
from store.models import Mobile, AppleWatch
import uuid

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_product = models.ForeignKey(Mobile, on_delete=models.CASCADE, null=True, blank=True)
    watch_product = models.ForeignKey(AppleWatch, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='cart/', blank=True)

    def get_product_name(self):
        return self.mobile_product.name if self.mobile_product else self.watch_product.name
    



class Purchased(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)
    processed = models.BooleanField(default=False)
    order_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    products = models.TextField()
    
    def __str__(self):
        return f'{self.user} - {self.first_name}'

