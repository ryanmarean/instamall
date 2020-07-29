from django.shortcuts import render, redirect

# Create your views here.
def index(render):
    return render(request,"homepage")