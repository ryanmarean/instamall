from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    # this is supposed 
    path('RoysMall', views.roy_mall, name='Roys Mall'),
    # <a href="{% url 'Roys Mall' %}">Roys Mall</a>, this belongs in templates
    path('roy_store', views.roy_store),
    path(''),
    path(''),
    path(''),

    
]
