from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail', views.cart_detail, name="cart_detail"),
    path('add/<int:pk>', views.cart_add, name="cart_add"),
    path('delete/<str:id>', views.cart_delete, name="cart_delete"),
]
