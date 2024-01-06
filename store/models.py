from django.db import models
from django.core.validators import EmailValidator
from PIL import Image
from django.core.exceptions import ValidationError
from datetime import datetime


class MobileCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Mobile Category'
        ordering = ('order',)

    def __iter__(self):
        mobiles = self.mobiles.filter(is_visible=True)
        for mobile in mobiles:
            yield mobile



    def __str__(self):
        return f'{self.name}'

class Mobile(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='mobile/', blank=True)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    category = models.ForeignKey(MobileCategory, on_delete=models.PROTECT, related_name ='mobiles') 


    def __str__(self):
        return f'{self.name}' 
    
    
    class Meta:
        verbose_name_plural = 'Mobiles'
        ordering = ('order',)
        constraints  = [
            models.UniqueConstraint(fields=['order', 'category'], name='unique_order_category')
        ]
        unique_together = ['id', 'slug']

class EmailSubscriber(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator(message='Enter a valid email')])

    def __str__(self):
        return self.email
    
class Banner(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='banner/')
    button_text = models.CharField(max_length=20)
    link = models.URLField()
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
    def validate_image_dimensions(self, value):
        max_width = 657  # max_width
        max_height = 677  # max_height

        with Image.open(value) as img:
            width, height = img.size
            if width > max_width or height > max_height:
                raise ValidationError(f"The size of the image must be smaller than or equal to {max_width}x{max_height} pixels.")

    def save(self, *args, **kwargs):
        self.validate_image_dimensions(self.photo)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Banner {self.id}'




