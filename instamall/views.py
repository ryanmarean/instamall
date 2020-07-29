from django.shortcuts import render, redirect


def index(render):
    return render(request, 'mall_lane.html')
    
def show_mall(request, mall_id):
    return render(request, 'show_mall.html')

def show_store(request, store_id):
    return render(request, 'show_store.html')

def shopping_cart(request):
    return render(request, 'shopping_cart.html')

def purchase_complete(request):
    return render(request, 'purchase_complete.html')