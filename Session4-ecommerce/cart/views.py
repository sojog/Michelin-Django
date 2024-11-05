from django.shortcuts import render, redirect
from shop.models import Product
from .forms import ProductToCartForm
# Create your views here.

def cart_view(request):
    cart_product_pks = request.session.get('cart', {})
    if cart_product_pks:
        cart_product_pks = cart_product_pks.keys()
   
    print("Product primary keys=", cart_product_pks)

    products = Product.objects.filter(id__in = cart_product_pks)

    #[ prod1, prod2]
    #[(prod1, qty1), (prod2, qty2)]

    products_quantities = [(prod, request.session.get('cart')[f'{prod.id}']) for prod in products]
    context = {
        'products_quantities': products_quantities
    }
    return render(request, "cart.html",context)


def add_to_cart_view(request, pk):
    
    if not request.session.get('cart'):
        request.session['cart'] = {   }    ## "pk1" : 3 # 3 products

    form = ProductToCartForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data["quantity"]

        request.session['cart'][pk] = request.session['cart'].get(pk, 0) + int(quantity)

        print("after adding the key:", request.session['cart'])

        request.session.modified = True

        product_to_be_added = Product.objects.get(pk=pk)

        print("I need to add this product to cart", product_to_be_added)

    return redirect("cart_url")


def empty_cart_view(request):
    request.session['cart'] = {   } 
    request.session.modified = True

    return redirect("cart_url")