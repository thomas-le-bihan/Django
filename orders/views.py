from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from orders.forms import OrderForm
from .models import Order


def list(request):
    """
    Display a list of orders
    """
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']
        orders = Order.objects.filter(
            Q(order_id=query) | Q(order_mrid=query) |
            Q(order_refid=query) | Q(order_amount=query) |
            Q(marketplace=query))
    else:
        orders = Order.objects.all()

    total_orders = len(Order.objects.all())

    context = {
        'title': 'Order list',
        'orders': orders,
        'total_order': total_orders,
    }
    return render(request, 'orders/list.html', context)


def change(request, order_id=''):
    """
    Display a single order
    """
    if order_id is not '':
        order = get_object_or_404(Order, pk=order_id)
    else:
        order = None

    if request.method == 'POST':
        if order is None:
            order_form = OrderForm(request.POST)
        else:
            order_form = OrderForm(request.POST, instance=order)
        if order_form.is_valid():
            order = order_form.save()
            print(order)
            return HttpResponseRedirect('/orders/list/')
    else:
        if order is None:
            order_form = OrderForm()
        else:
            order_form = OrderForm(instance=order)

    context = {
        'title': 'Change order',
        'order_id': order_id,
        'order_form': order_form,
    }
    return render(request, 'orders/change.html', context)
