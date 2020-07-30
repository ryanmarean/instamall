from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    # request.session['uid'] = 1
    return render(request, 'mall_lane.html')
    
def show_mall(request, mall_id):
    return render(request, 'show_mall.html')

def show_store(request, mall_id, store_id):
    this_store = Store.objects.get(id=store_id)
    context = {
        "this_store" : this_store,
        "products" : this_store.products.all(),
        "mall_id" : mall_id,
        "store_id" : store_id,
    }
    return render(request, 'show_store.html',context)

def add_to_cart(request, mall_id, store_id, product_id):
    if product_id in request.session['cart']:
        currQ = request.session['cart'][product_id]
        currQ += int(request.POST['quantity'])
        request.session['cart'][product_id] = currQ
    else:
        request.session['cart'][product_id] = int(request.POST['quantity'])
    messages.success(request, "Item added to cart!")
    print(request.session['cart'])
    return redirect ('/mall/' + str(mall_id) + '/' + str(store_id))

def shopping_cart(request):
    context = {
        'cart' : request.session['cart'],
    }
    print(request.session['cart'])
    return render(request, 'shopping_cart.html',context)

def checkout(request):
    for product_id, quantity in request.session['cart'].items():
        product = Product.objects.get(id=product_id)
        price = product.price
        request.session['order'] += {
            "product_id" : [product],
            "price_each" : price,
            "amount_purchased" : quantity,
            "total_price" : quantity * price
        }
        request.session['cart'].flush()
        print(request.session['order'])
    return redirect('/purchase_complete')

def purchase_complete(request):
    context = {
        "all_products" : Products.objects.all()
    }
    return render(request, 'purchase_complete.html', context)