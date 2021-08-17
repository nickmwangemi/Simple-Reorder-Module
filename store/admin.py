from django.contrib import admin
from .models import Product, Reorder

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

class ReorderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Reorder, ReorderAdmin)
