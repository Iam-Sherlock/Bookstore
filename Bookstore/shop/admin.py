from django.contrib import admin
from .models import category,Product
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=['bname','description','created_at']
class ProductAdmin(admin.ModelAdmin):
    list_display=['bname','category','quantity','created_at']
admin.site.register(category,categoryAdmin)
admin.site.register(Product,ProductAdmin)