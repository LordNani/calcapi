from django.urls import path

from . import views

urlpatterns = [
    path('sum', views.sum, name='sum'),
    path('subtract', views.subtract, name='subtract'),
    path('divide', views.divide, name='divide'),
    path('product', views.product, name='product')
]