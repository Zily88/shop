from django.shortcuts import render
from .models import ProductItem, ProductSex, ProductSubCategory, ProductCategory, ProductSubSubCategory, Tags, Review
from cart.models import CartProduct

# Create your views here.

def index(request):
    title = 'Home'
    content = {}
    content['title'] = title
    new_in_men = {
        'NEW IN' : [ProductCategory.objects.get(title='Men Clothing'), ProductSubCategory.objects.get(title='Men Bags'),
                  ProductSubCategory.objects.get(title='Men Shoes'), ProductSubCategory.objects.get(title='Men Watches'),
                  ProductCategory.objects.get(title='Grooming')]}
    clothing_men = {'CLOTHING' : ProductSubSubCategory.objects.filter(
        parent_sub_category__parrent_category__title = 'Men Clothing').filter(position__gt=0).order_by('position')}
    watches_men = {'WATCHES' : ProductSubSubCategory.objects.filter(parent_sub_category__title = 'Men Watches').
        filter(position__gt=0).order_by('position')}
    new_in_women = {
        'NEW IN': [ProductCategory.objects.get(title='Women Clothing'), ProductSubCategory.objects.get(title='Women Bags'),
                   ProductSubCategory.objects.get(title='Women Shoes'),
                   ProductSubCategory.objects.get(title='Women Watches'),
                   ProductCategory.objects.get(title='Beauty')]}
    clothing_women = {'CLOTHING': ProductSubSubCategory.objects.filter(
        parent_sub_category__parrent_category__title='Women Clothing').filter(position__gt=0).order_by('position')}
    watches_women = {
        'WATCHES': ProductSubSubCategory.objects.filter(parent_sub_category__title='Women Watches').
            filter(position__gt=0).order_by('position')}
    new_in_kids = {
        'NEW IN': [ProductCategory.objects.get(title='Boys Clothing'),
                   ProductCategory.objects.get(title='Girls Clothing'),
                   ProductSubCategory.objects.get(title='Boys Shoes'),
                   ProductSubCategory.objects.get(title='Girls Shoes')]}
    accesories_kids = {
        'Accesories' : ProductSubCategory.objects.filter(parrent_category__title='Kids Accesories').
            filter(position__gt=0).order_by('position')}
    menu = {}
    men = {}
    men.update(new_in_men)
    men.update(clothing_men)
    men.update(watches_men)
    women = {}
    women.update(new_in_women)
    women.update(clothing_women)
    women.update(watches_women)
    kids = {}
    kids.update(new_in_kids)
    kids.update(accesories_kids)
    menu['men'] = men
    menu['women'] = women
    menu['kids'] = kids
    content['menu'] = menu
    latest_products = ProductItem.objects.order_by('present_date')[:9]
    content['latest_products'] = latest_products
    featured_collections = ProductItem.objects.filter(featured_collection=True)
    content['featured_collections'] = featured_collections
    # sex = ProductSex.objects.filter(visible_in_nav=True).order_by('left_to_right')
    # content['sex'] = sex
    # categories = ProductCategory.objects.filter(visible_in_nav=True).order_by('up_to_down')
    # content['categories'] = categories
    user = request.user
    session = request.session
    if user.is_authenticated:
        cart = CartProduct.objects.filter(user=user)
        if cart:
            cart = cart[0]
            price = CartProduct.get_price(cart)
            quantity = CartProduct.get_quantity(cart)
        else:
            price = 0
            quantity = 0
    else:
        try:
            products = ProductItem.objects.filter(pk__in=session['cart'])
            price = 0
            for item in products:
                price += item.price
            quantity = len(products)
        except KeyError:
            price = 0
            quantity = 0

    content['price'] = price
    content['quantity'] = quantity
    return render(request, 'mainapp/index.html', content)

def products(request, cat):
    title = 'Products'
    content = {}
    # print(request.path_info)
    if 'category' in request.path_info:
        product_items = ProductItem.objects.filter(sub_sub_category__parent_sub_category__parrent_category__visible_name=cat).\
            order_by('rating')
    if 'subcategory' in request.path_info:
        product_items = ProductItem.objects.filter(sub_sub_category__parent_sub_category__visible_name=cat).\
            order_by('rating')
    if 'subsubcategory' in request.path_info:
        product_items = ProductItem.objects.filter(sub_sub_category=cat).\
            order_by('rating')
    new_in_men = {
        'NEW IN': [ProductCategory.objects.get(title='Men Clothing'), ProductSubCategory.objects.get(title='Men Bags'),
                   ProductSubCategory.objects.get(title='Men Shoes'),
                   ProductSubCategory.objects.get(title='Men Watches'),
                   ProductCategory.objects.get(title='Grooming')]}
    clothing_men = {'CLOTHING': ProductSubSubCategory.objects.filter(
        parent_sub_category__parrent_category__title='Men Clothing').filter(position__gt=0).order_by('position')}
    watches_men = {
        'WATCHES': ProductSubSubCategory.objects.filter(parent_sub_category__title='Men Watches').
            filter(position__gt=0).order_by('position')}
    new_in_women = {
        'NEW IN': [ProductCategory.objects.get(title='Women Clothing'),
                   ProductSubCategory.objects.get(title='Women Bags'),
                   ProductSubCategory.objects.get(title='Women Shoes'),
                   ProductSubCategory.objects.get(title='Women Watches'),
                   ProductCategory.objects.get(title='Beauty')]}
    clothing_women = {'CLOTHING': ProductSubSubCategory.objects.filter(
        parent_sub_category__parrent_category__title='Women Clothing').filter(position__gt=0).order_by('position')}
    watches_women = {
        'WATCHES': ProductSubSubCategory.objects.filter(parent_sub_category__title='Women Watches').
            filter(position__gt=0).order_by(
            'position')}
    new_in_kids = {
        'NEW IN': [ProductCategory.objects.get(title='Boys Clothing'),
                   ProductCategory.objects.get(title='Girls Clothing'),
                   ProductSubCategory.objects.get(title='Boys Shoes'),
                   ProductSubCategory.objects.get(title='Girls Shoes')]}
    accesories_kids = {
        'Accesories': ProductSubCategory.objects.filter(parrent_category__title='Kids Accesories').
            filter(position__gt=0).order_by('position')}
    menu = {}
    men = {}
    men.update(new_in_men)
    men.update(clothing_men)
    men.update(watches_men)
    women = {}
    women.update(new_in_women)
    women.update(clothing_women)
    women.update(watches_women)
    kids = {}
    kids.update(new_in_kids)
    kids.update(accesories_kids)
    menu['men'] = men
    menu['women'] = women
    menu['kids'] = kids
    content['menu'] = menu
    content['product_items'] = product_items
    return render(request, 'mainapp/products.html', content)

def contact(request):
    return render(request, 'mainapp/contact.html')

def single(request, pk):
    content = {}
    product_item = ProductItem.objects.get(pk=pk)
    content['product_item'] = product_item
    reviews = Review.objects.filter(product=product_item)
    content['reviews'] = reviews
    new_in_men = {
        'NEW IN': [ProductCategory.objects.get(title='Men Clothing'), ProductSubCategory.objects.get(title='Men Bags'),
                   ProductSubCategory.objects.get(title='Men Shoes'),
                   ProductSubCategory.objects.get(title='Men Watches'),
                   ProductCategory.objects.get(title='Grooming')]}
    clothing_men = {'CLOTHING': ProductSubSubCategory.objects.filter(
        parent_sub_category__parrent_category__title='Men Clothing').filter(position__gt=0).order_by('position')}
    watches_men = {
        'WATCHES': ProductSubSubCategory.objects.filter(parent_sub_category__title='Men Watches').
            filter(position__gt=0).order_by('position')}
    new_in_women = {
        'NEW IN': [ProductCategory.objects.get(title='Women Clothing'),
                   ProductSubCategory.objects.get(title='Women Bags'),
                   ProductSubCategory.objects.get(title='Women Shoes'),
                   ProductSubCategory.objects.get(title='Women Watches'),
                   ProductCategory.objects.get(title='Beauty')]}
    clothing_women = {'CLOTHING': ProductSubSubCategory.objects.filter(
        parent_sub_category__parrent_category__title='Women Clothing').filter(position__gt=0).order_by('position')}
    watches_women = {
        'WATCHES': ProductSubSubCategory.objects.filter(parent_sub_category__title='Women Watches').
            filter(position__gt=0).order_by(
            'position')}
    new_in_kids = {
        'NEW IN': [ProductCategory.objects.get(title='Boys Clothing'),
                   ProductCategory.objects.get(title='Girls Clothing'),
                   ProductSubCategory.objects.get(title='Boys Shoes'),
                   ProductSubCategory.objects.get(title='Girls Shoes')]}
    accesories_kids = {
        'Accesories': ProductSubCategory.objects.filter(parrent_category__title='Kids Accesories').
            filter(position__gt=0).order_by('position')}
    menu = {}
    men = {}
    men.update(new_in_men)
    men.update(clothing_men)
    men.update(watches_men)
    women = {}
    women.update(new_in_women)
    women.update(clothing_women)
    women.update(watches_women)
    kids = {}
    kids.update(new_in_kids)
    kids.update(accesories_kids)
    menu['men'] = men
    menu['women'] = women
    menu['kids'] = kids
    content['menu'] = menu
    return render(request, 'mainapp/single.html', content)