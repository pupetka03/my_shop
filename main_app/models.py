from django.db import models
from django.urls import reverse


class MainMenuItems(models.Model):
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='url')
    url = models.CharField(max_length=180, blank=True) 
    is_anchor = models.BooleanField(default=False)
    is_manager_only = models.BooleanField(default=False)
    is_visible = models.BooleanField(default =True)
    order = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        if self.is_anchor:
            return reverse('store:home') + f'#{self.slug}'
        
        return f'/{self.slug}/'

    def __str__(self):
        return f'{self.title}/{self.slug}'

    class Meta:
        ordering = ('order',)
        