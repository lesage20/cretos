from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
import json
from account.models import Customer, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from shop.models import Categorie, Produit


# global variable


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer, complete=False)
        orders_count = orders.count()
        items = []
        
        produit_total_command = int()
        prix_total = int()
        
        for order in orders:
            items += OrderItem.objects.filter(order=order)
            dir(order.produits)
            for item in items:
                produit_total_command += item.quantity
                prix_total += item.get_total_price
                
    else:
        return redirect('login')
        
    
    datas = {
        'items':items,
        'orders_count':orders_count,
        'produit_total_command': produit_total_command,
        'prix_total':prix_total
    }
    return render(request, 'account/cart.html', datas)

def products(request):
    
    produit = Produit.objects.filter(status=True)

    datas = {
        "produit":produit,
    }


    return render(request, 'shop/shop.html', datas)

def product(request, id):
    single = get_object_or_404(Produit, id=id)
    produits = Produit.objects.filter(status=True)[:5]

    

    datas= {

        "single": single,
        'produits': produits
    }
    return render(request, 'shop/single-shop.html', datas)

def addToCart(request, id):

    try:
        customer = request.user.customer
        produit = get_object_or_404(Produit, id=id)
        orders = Order.objects.filter(customer=customer, complete=False)
        
        orderItem, created = OrderItem.objects.get_or_create(produit=produit,customer=customer)
        
        if orders.exists():
            order = orders[0]
            
            if order.produits.filter(produit__id=produit.id).exists():
                orderItem.quantity += 1
                orderItem.save()
            else:
                order.produits.add(orderItem)  
        else:
            order = Order.objects.create(customer=customer, date_add=timezone.now())
            order.produits.add(orderItem)
            order.save()
            

    except ValueError as e:
            print(e)
    
    return redirect('cart')