from django.contrib import admin
from django.db import models
from django.forms import Textarea 
from .models import MobileCategory, Mobile, AppleWatch, WatchCategory, EmailSubscriber, Banner, BannerPromo
from django.utils.safestring import mark_safe


admin.site.register(MobileCategory)
admin.site.register(EmailSubscriber)
admin.site.register(WatchCategory)

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("id", "category", "name", "price",  "is_visible", "photo_src_tag")
    list_editable = ("category", "name", "price",  "is_visible")
    search_fields = ('name',)
    list_filter = ('category', "price", "is_visible",)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Mobile photo'

    
@admin.register(AppleWatch)
class AppleWatchAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("id", "category", "name", "price",  "is_visible", "photo_src_tag")
    list_editable = ("category", "name", "price",  "is_visible")
    search_fields = ('name',)
    list_filter = ('category', "price", "is_visible",)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Watch photo'

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "button_text", "link", "is_visible", "order", "start_date", "end_date")
    list_editable = ("text", "button_text", "link", "is_visible", "order", "start_date", "end_date")
    search_fields = ('text',)
    list_filter = ("is_visible", "order", "start_date", "end_date")
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


@admin.register(BannerPromo)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "button_text", "link", "is_visible", "order", "photo")
    list_editable = ("text", "button_text", "link", "is_visible", "order", "photo")
    search_fields = ('text',)
    list_filter = ("is_visible", "order",)
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


