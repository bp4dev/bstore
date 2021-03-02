import json
from .models import *

def cookieCart(request):
    #render cart total
    #try fixes temp bug and set cart once page is loaded
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']
    #loop through cart and add cart items
    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            #create dictionary rep of order item for guest users 
            # includes all the same attributes in OrderItem model

            item = {
                'product':{
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'imageURL':product.imageURL,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total,
                }
            items.append(item)

            #shipping info
            if product.digital == False:
                order['Shipping'] = True   
        except:
            pass 
    return{'cartItems' :cartItems, 'order':order, 'items':items}