from django.contrib import admin
from .models import ProductCategory, ProductItem, ProductSex, ProductSubCategory, ProductSubSubCategory, Tags, AdminProductCategory, AdminProductItem, AdminProductSubCategory, AdminProductSubSubCategory, Review

# Register your models here.

admin.site.register(ProductSex)
admin.site.register(ProductCategory, AdminProductCategory)
admin.site.register(ProductItem, AdminProductItem)
admin.site.register(ProductSubCategory, AdminProductSubCategory)
admin.site.register(ProductSubSubCategory, AdminProductSubSubCategory)
admin.site.register(Tags)
admin.site.register(Review)