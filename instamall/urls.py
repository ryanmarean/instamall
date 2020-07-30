from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('mall/<int:mall_id>', views.show_mall),
    path('mall/<int:mall_id>/<int:store_id>', views.show_store),
    path('mall/<int:mall_id>/<int:store_id>/add_to_cart/<int:product_id>',views.add_to_cart),
    path('shopping_cart', views.shopping_cart),
    path('checkout',views.checkout),
    path('purchase_complete', views.purchase_complete),
]

