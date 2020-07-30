from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
        request.session['product_amount'] = 0

    return render(request, 'mall_lane.html')
    
def show_mall(request, mall_id):
    if 'cart' not in request.session:
        return redirect('/')

    context = {
        "this_mall" : Mall.objects.get(id=mall_id)
    }

    return render(request, 'show_mall.html',context)

def show_store(request, mall_id, store_id):
    if 'cart' not in request.session:
        return redirect('/')

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
    if 'cart' not in request.session:
        return redirect('/')

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
    total_amount = 0
    for product in request.session['cart']:
        charging_product = Product.objects.get(id=product)
        total_amount += charging_product.price * request.session['cart'][str(charging_product.id)]
    print(total_amount)

    context = {
        'stores_visited' : stores_visited,
        'products_added' : products_added,
        'total_amount' : total_amount,
        'cart' : request.session['cart'],
        'all_products' : Product.objects.all(),
    }
    print(request.session['cart'])

    return render(request, 'shopping_cart.html',context)

def remove_product(request, product_id):
    request.session['product_amount'] -= request.session['cart'][str(product_id)]
    request.session['cart'].pop(str(product_id))
    return redirect('/shopping_cart')

def add_product(request,product_id):
    request.session['cart'][str(product_id)] += 1
    request.session['product_amount'] += 1
    return redirect('/shopping_cart')

def decrease_product(request, product_id):
    if request.session['cart'][str(product_id)] == 1:
        return redirect('/remove_product/' + str(product_id))
    request.session['cart'][str(product_id)] -= 1
    request.session['product_amount'] -= 1
    return redirect('/shopping_cart')


def purchase_complete(request):
    stores_visited = [] # list of Store objects
    for product_id in request.session['cart']:
        this_product = Product.objects.get(id=product_id)
        if this_product.store not in stores_visited:
            stores_visited.append(this_product.store)
    print(stores_visited)
    products_added = [] # list of Product objects
    for product_id in request.session['cart']:
        this_product = Product.objects.get(id=product_id)
        products_added.append(this_product)
    print(products_added)
    total_amount = 0
    for product in request.session['cart']:
        charging_product = Product.objects.get(id=product)
        total_amount += charging_product.price * request.session['cart'][str(charging_product.id)]
    print(total_amount)
    context = {
        'stores_visited' : stores_visited,
        'products_added' : products_added,
        'total_amount' : total_amount,
        'cart' : request.session['cart'],
        'all_products' : Product.objects.all(),
    }
    request.session.flush()
    request.session['cart'] = {}
    request.session['product_amount'] = 0
    print(request.session['cart'])
    return render(request, 'purchase_complete.html', context)