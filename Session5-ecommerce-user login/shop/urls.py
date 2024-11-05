
from django.urls import path
from .views import product_list_view, product_details_view, ProductListView, ProductDetailView, CategoryListView,CategoryDetailView

## SHOP APP
urlpatterns = [
    path('list', product_list_view),

    path('categories', CategoryListView.as_view()),
    path('categories/<slug>',CategoryDetailView.as_view(), name="category_details_url"),
    
    path('classlist', ProductListView.as_view()),
    path('details/<slug>',  product_details_view, name="details_url"), # http://127.0.0.1:8000/details/second-product,
    path('classdetails/<slug>',  ProductDetailView.as_view()) 
]


