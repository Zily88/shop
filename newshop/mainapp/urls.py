from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('category/<str:cat>', mainapp.products, name='category'),
    path('subcategory/<str:cat>', mainapp.products, name='subcategory'),
    path('subsubcategory/<str:cat>', mainapp.products, name='subsubcategory'),
    path('', mainapp.products, name='index'),
    path('<int:pk>', mainapp.single, name='product'),
]