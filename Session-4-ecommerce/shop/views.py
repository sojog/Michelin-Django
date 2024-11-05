from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
from cart.forms import ProductToCartForm





def product_list_view(request):

    products = Product.objects.all()
    context = {
        'products':products,
 
    }
    return render(request, 'product_list.html', context)

def product_details_view(request, slug):

    product = get_object_or_404(Product, slug=slug)

    product_to_cart_form = ProductToCartForm()

    context = {
        'product':product,
        'product_to_cart_form' : product_to_cart_form
    }
    return render(request, 'product_details.html', context)