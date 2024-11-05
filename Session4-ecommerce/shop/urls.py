
from django.urls import path
from .views import product_list_view, product_details_view

## SHOP APP
urlpatterns = [
    path('list', product_list_view),
    path('details/<slug>',  product_details_view, name="details_url") # http://127.0.0.1:8000/details/second-product
]


