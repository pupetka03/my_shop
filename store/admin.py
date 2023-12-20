from django.contrib import admin
from .models import MobileCategory, Mobile


admin.site.register(MobileCategory)

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'category', 'name', 'price',  "is_visible")
    
    # slug
    # description  
    # photo
    # order


    
    
