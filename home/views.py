from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

import datetime
import json

from .forms import StatusForm
from .models import *
from .utils import cookieCart, cartData, guestOrder

def malina_home(request):

    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(main_page=True)
    products = Product.objects.all()

    return render(request, 'home/index.html', {'products': products, 'cartItems': cartItems, 'categories': categories,})

def dop_menu(request):
    data = cartData(request)
    cartItems = data['cart_items']
    return render(request, 'home/dop_menu.html', {'cartItems': cartItems})

def dop_menu_mon(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(menu_monday=True)
    products = Product.objects.all()

    return render(request, 'home/dop_menu_mon.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def dop_menu_tue(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(menu_tuesday=True)
    products = Product.objects.all()

    return render(request, 'home/dop_menu_tue.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def dop_menu_wed(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(menu_wednesday=True)
    products = Product.objects.all()

    return render(request, 'home/dop_menu_wed.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def dop_menu_thu(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(menu_thursday=True)
    products = Product.objects.all()

    return render(request, 'home/dop_menu_thu.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def dop_menu_fri(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(menu_friday=True)
    products = Product.objects.all()

    return render(request, 'home/dop_menu_fri.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def delivery(request):
    data = cartData(request)
    cartItems = data['cart_items']
    return render(request, 'home/delivery.html', {'cartItems': cartItems})

def complex_delivery(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(complex_delivery=True)
    products = Product.objects.all()

    return render(request, 'home/complex_delivery.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def vip_delivery(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(vip_delivery=True)
    products = Product.objects.all()

    return render(request, 'home/vip_delivery.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def banket_delivery(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(banket_delivery=True)
    products = Product.objects.all()

    return render(request, 'home/banket_delivery.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def children_delivery(request):
    data = cartData(request)
    cartItems = data['cart_items']
    categories = Category.objects.filter(children_delivery=True)
    products = Product.objects.all()

    return render(request, 'home/children_delivery.html', {'products': products, 'cartItems': cartItems, 'categories': categories})

def about(request):
    data = cartData(request)
    cartItems = data['cart_items']
    return render(request, 'home/about.html', {'cartItems': cartItems})

def contact(request):
    data = cartData(request)
    cartItems = data['cart_items']
    return render(request, 'home/contact.html', {'cartItems': cartItems})

def cart(request):

    data = cartData(request)
    cartItems = data['cart_items']
    order = data['order']
    items = data['items']

    return render(request, 'home/cart.html', {'items': items, 'order': order, 'cartItems': cartItems})

def checkout(request):


    data = cartData(request)
    cartItems = data['cart_items']
    order = data['order']
    items = data['items']

    return render(request, 'home/checkout.html', {'items': items, 'order': order, 'cartItems': cartItems})

def conditions(request):
    data = cartData(request)
    cartItems = data['cart_items']

    return render(request, 'home/conditions.html', {'cartItems': cartItems})

def adminpanel(request):
    addresses_list = ShippingAddress.objects.all().order_by('-id')
    items = OrderItem.objects.all()

    paginator = Paginator(addresses_list, 10)
    page = request.GET.get('page')

    try:
        addresses = paginator.page(page)
    except PageNotAnInteger:
        addresses = paginator.page(1)
    except EmptyPage:
        addresses = paginator.page(paginator.num_pages)

    return render(request, 'home/adminpanel.html', {'addresses': addresses, 'items': items})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

#from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
def checkout_cash(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(str(data['form']['total']).strip().replace(',', '.'))
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        name=data['form']['name'],
        sec_name=data['form']['sec_name'],
        company=data['form']['company'],
        email=data['form']['email'],
        address=data['form']['address'],
        phone=data['form']['phone'],
        consent=data['form']['consent'],
        question=data['form']['question'],
        note=data['form']['note'],

        name_2=data['form']['name_2'],
        sec_name_2=data['form']['sec_name_2'],
        company_2=data['form']['company_2'],
        address_2=data['form']['address_2'],
        phone_2=data['form']['phone_2'],
        status='New',

    )

    return JsonResponse('Успешно', safe=False)