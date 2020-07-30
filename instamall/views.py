from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
        request.session['product_amount'] = 0

    return render(request, 'mall_lane.html')
    
def show_mall(request, mall_id):
    return render(request, 'show_mall.html')

def show_store(request, mall_id, store_id):
    this_store = Store.objects.get(id=store_id)
    if store_id == 1:
        bg_source = "Clint_Salts.png"
    if store_id == 2:
        bg_source = "Beth.jpg"
    if store_id == 3:
        bg_source = "benjamin.png"
    if store_id == 4:
        bg_source = "Wilson_suits.png"
    if store_id == 5:
        bg_source = "mogi_shoes.png"
    if store_id == 6:
        bg_source = "Josh_Adrian_Bakery.png"

    context = {
        "this_store" : this_store,
        "products" : this_store.products.all(),
        "mall_id" : mall_id,
        "store_id" : store_id,
        "bg_source": bg_source,
    }
    return render(request, 'show_store.html',context)

def add_to_cart(request, mall_id, store_id, product_id):
    if str(product_id) in request.session['cart']:
        currQ = request.session['cart'][str(product_id)]
        currQ += int(request.POST['quantity'])
        request.session['cart'][str(product_id)] = currQ
        request.session['product_amount'] += int(request.POST['quantity'])
        request.session.save()
    else:
        request.session['cart'][str(product_id)] = int(request.POST['quantity'])
        request.session['product_amount'] += int(request.POST['quantity'])
        request.session.save()
    messages.success(request, "Item added to cart!")
    print(request.session['cart'])
    return redirect ('/mall/' + str(mall_id) + '/' + str(store_id))

def shopping_cart(request):

    stores_visited = []
    for product_id in request.session['cart']:
        this_product = Product.objects.get(id=product_id)
        if this_product.store not in stores_visited:
            stores_visited.append(this_product.store)
    print(stores_visited)
    products_added = []
    for product_id in request.session['cart']:
        this_product = Product.objects.get(id=product_id)
        products_added.append(this_product)
    print(products_added)
    context = {
        'stores_visited' : stores_visited,
        'products_added' : products_added,
        'cart' : request.session['cart'],
        'all_products' : Product.objects.all(),
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