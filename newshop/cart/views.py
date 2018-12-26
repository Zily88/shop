from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import CartProduct, ProductItem
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
import json

# Create your views here.

def cart(request):
    content = {}
    title = 'Cart'
    content['title'] = title
    user = request.user
    session = request.session
    if user.is_authenticated:
        cart_products = CartProduct.objects.filter(user=request.user)
        if cart_products:
            cart = cart_products[0]
            price = CartProduct.get_price(cart)
            quantity = CartProduct.get_quantity(cart)
        else:
            price = 0
            quantity = 0
    else:
        try:
            products = session['cart']
            cart_products = ProductItem.objects.filter(pk__in=session['cart'])
            price = 0
            for item in cart_products:
                price += item.price
            quantity = len(cart_products)
        except KeyError:
            cart_products = list()
            price = 0
            quantity = 0
    content['cart_products'] = cart_products
    content['price'] = price
    content['quantity'] = quantity
    return render(request, 'cart/checkout.html', content)

def cart_add(request, pk):
    if request.is_ajax():
        print('Is Ajax In ADD')
        product = get_object_or_404(ProductItem, pk=pk)
        user = request.user
        if user.is_authenticated:
            cart_product = CartProduct(user=request.user, product=product)
            cart_product.save()
            price = cart_product.get_price()
            quantity = cart_product.get_quantity()
        else:
            try:
                # request.session['cart'] = list()
                # request.session.save()

                print('IN TRY')
                session = request.session
                print(pk)
                session['cart'].append(str(pk))
                print(session['cart'])
                session.save()
                print(session['cart'])
                products = ProductItem.objects.filter(pk__in=session['cart'])
                quantity = len(products)
                price = 0
                for item in products:
                    price += item.price

                # data = serializers.serialize('json', ProductItem.objects.filter(pk=pk), fields=('title'))
                # print(data)
                # request.session['cart'].append(data)
                # request.session.save()
                # print(request.session['cart'])
                # price = 0
                # quantity = len(request.session['cart'])
                # print(request.session['cart'])
                # items = list()
                # for item in request.session['cart']:
                #     items.append(json.loads(item))
                # print(items)
                # items_pk = list()
                # for item in items:
                #     items_pk.append(item[0]['pk'])
                # print(items_pk)
                # products = ProductItem.objects.filter(pk__in=items_pk)
            except KeyError:
                session = request.session
                session['cart'] = list()
                session['cart'].append(str(pk))
                session.save()
                price = product.price
                quantity = 1
                # print(e)
                # print('---------------------------------------------------')
                # print('IN EXEPT')
                # print('---------------------------------------------------')
                # request.session['cart'] = list()
                # data = serializers.serialize('json', ProductItem.objects.filter(pk=pk), fields=('title'))
                # request.session['cart'].append(data)
                # print('---------------------------------------------------')
                # print(request.session['cart'])
                # print('---------------------------------------------------')
                # price = product.price
                # quantity = 1
                # print('---------------------------------------------------')
                # print(price, quantity)
                # print('---------------------------------------------------')
                # request.session.save()
        return JsonResponse({'price': price, 'quantity': quantity})
    # print('before')
    # print(request, pk)
    # product = get_object_or_404(ProductItem, pk=pk)
    # print('after', product.price)
    # print(product)
    # cart_product = CartProduct(user=request.user, product=product)
    # cart_product.save()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart_remove(request, pk):
    if request.is_ajax():
        user = request.user
        session = request.session
        if user.is_authenticated:
            # print('Is Ajax')
            cart_product = CartProduct.objects.get(pk=pk)
            cart_product.delete()
            cart = CartProduct.objects.filter(user=request.user)
            if cart:
                cart = cart[0]
                quantity = CartProduct.get_quantity(cart)
                price = CartProduct.get_price(cart)
            else:
                quantity = 0
                price = 0
        else:
            session['cart'].remove(str(pk))
            session.save()
            cart_products = ProductItem.objects.filter(pk__in=session['cart'])
            if len(cart_products):
                quantity = len(cart_products)
                price = 0
                for item in cart_products:
                    price += item.price
            else:
                quantity = 0
                price = 0
        # print(quantity)
        return JsonResponse({'quantity': quantity, 'price': price})