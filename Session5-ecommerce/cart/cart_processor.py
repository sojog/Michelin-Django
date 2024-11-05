

def processesing(request):
    product_dictionary = request.session.get('cart', {})
    total_items = sum(product_dictionary.values())
    return {
        'total_items':total_items
    }
    