from django.db import models
from django.core.exceptions import ValidationError
from django.contrib import admin
from authapp.models import ShopUser

# Create your models here.

class ProductCategory(models.Model):

    title = models.CharField(max_length=32, unique=True)
    sex = models.ForeignKey('ProductSex', on_delete=models.CASCADE)
    visible_name = models.CharField(max_length=32)
    position = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class AdminProductCategory(admin.ModelAdmin):

    list_display = ('title', 'sex', 'visible_name', 'position')

class ProductSex(models.Model):

    title = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.title

class ProductSubCategory(models.Model):

    title = models.CharField(max_length=32, unique=True)
    parrent_category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    visible_name = models.CharField(max_length=32)
    position = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class AdminProductSubCategory(admin.ModelAdmin):

    list_display = ('title', 'parrent_category', 'visible_name', 'position')

class ProductSubSubCategory(models.Model):

    title = models.CharField(max_length=32, unique=True)
    parent_sub_category = models.ForeignKey('ProductSubCategory', on_delete=models.CASCADE)
    visible_name = models.CharField(max_length=32)
    position = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class AdminProductSubSubCategory(admin.ModelAdmin):

    list_display = ('title', 'parent_sub_category', 'visible_name', 'position')

class Tags(models.Model):

    title = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title

class Review(models.Model):

    text = models.TextField()
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    product = models.ForeignKey('ProductItem', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class ProductItem(models.Model):

    title = models.CharField(max_length=32, unique=True)
    rating = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    present_date = models.DateTimeField(auto_now_add=True)
    main_img = models.ImageField(upload_to='product_image')
    left_img = models.ImageField(upload_to='product_image')
    middle_img = models.ImageField(upload_to='product_image')
    right_img = models.ImageField(upload_to='product_image')
    description = models.TextField()
    short_description = models.TextField()
    count_size_s = models.PositiveSmallIntegerField()
    count_size_m = models.PositiveSmallIntegerField()
    count_size_l = models.PositiveSmallIntegerField()
    sub_sub_category = models.ForeignKey('ProductSubSubCategory', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tags', blank=True)
    more_information = models.TextField()
    specification = models.TextField()
    featured_collection = models.BooleanField(default=False)
    made_in = models.CharField(max_length=32)
    fabric_origin = models.CharField(max_length=32)
    color = models.CharField(max_length=32)


    def __str__(self):
        return self.title

class AdminProductItem(admin.ModelAdmin):

    list_display = ('title', 'sub_sub_category', 'main_img',
                    'price', 'rating', 'present_date', 'count_size_s', 'featured_collection')


