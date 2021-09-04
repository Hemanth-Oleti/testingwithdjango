from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import *

def index(request):
    #for fields with ForeignKey(select_related)
    #orders = Order.objects.select_related('customer').all()
    #for order in orders:
        #temp = order.customer
    #for fields with ManyToMany Key Relation(prefetch_related)
    orders = Order.objects.prefetch_related('products').all()
    for i in orders:
        for p in i.products.all():
            temp = p
    return render(request, 'index.html')