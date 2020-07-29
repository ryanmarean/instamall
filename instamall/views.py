from django.shortcuts import render, redirect

# Create your views here.
def index(render):
    return render(request, "homepage")
    
def roy_mall(request):
    return redirect('/roy_store')

#this will be function for Roys stores
def roy_store(request):
    pass