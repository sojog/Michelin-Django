from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.
from cart.forms import ProductToCartForm

from django.views.generic import ListView, DetailView

# Function based view
def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'product_list.html', context)

# Class based view
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

# Function based view
def product_details_view(request, slug):

    product = get_object_or_404(Product, slug=slug)
    product_to_cart_form = ProductToCartForm()
    context = {
        'product':product,
        'product_to_cart_form' : product_to_cart_form
    }
    return render(request, 'product_details.html', context)

# Class based view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_to_cart_form = ProductToCartForm()
        context['product_to_cart_form'] = product_to_cart_form
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_details.html'
    context_object_name = 'category'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_category = self.get_object()
        print("The current category:", current_category)
        products_from_category = Product.objects.filter(category=current_category)
        print(products_from_category)
        context['products'] = products_from_category
        return context