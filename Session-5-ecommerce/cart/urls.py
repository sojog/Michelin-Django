from django.urls import path
from .views import cart_view, add_to_cart_view, empty_cart_view

urlpatterns = [ 
    path('', cart_view, name="cart_url"), 
    path('add/<pk>', add_to_cart_view, name="add_to_cart_url"),
    path('empty', empty_cart_view, name="empty_cart_url")
]