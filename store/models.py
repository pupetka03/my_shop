from django.db import models

class MobileCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

