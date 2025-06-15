from .cart import Cart

#Create a context processor so our cart is available on all pages of site
def cart(request):
    #Return the default data from our cart
    return {'cart': Cart(request)}
