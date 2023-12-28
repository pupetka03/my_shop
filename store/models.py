from django.db import models

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

from django.db import models

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


        
    
        
    