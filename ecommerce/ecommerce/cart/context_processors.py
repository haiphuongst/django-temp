from .cart import Cart

def cart_total_quantity(request):
    cart = Cart(request)
    return {'cart_total_quantity': len(cart)}