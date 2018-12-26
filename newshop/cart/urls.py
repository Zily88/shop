from django.urls import path

import cart.views as cart

app_name = 'cart'

urlpatterns = [
    path('', cart.cart, name='main'),
    path('add/<int:pk>', cart.cart_add, name='add'),
    path('remove/<int:pk>', cart.cart_remove, name='remove')
]