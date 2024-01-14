from django.db import models
from django.contrib.auth.models import User
from store.models import Mobile, AppleWatch

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_product = models.ForeignKey(Mobile, on_delete=models.CASCADE, null=True, blank=True)
    watch_product = models.ForeignKey(AppleWatch, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='cart/', blank=True)

    def get_product_name(self):
        return self.mobile_product.name if self.mobile_product else self.watch_product.name