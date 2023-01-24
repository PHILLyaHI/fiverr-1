from django.shortcuts import render
from item.models import Item, DeliveryOrder
from item.forms import ItemForm, DeliveryOrderForm, InvoiceForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


#Salesman System
def menu(request):
    items = Item.objects.all().order_by('-id')
    return render(request, "items/item_list.html", {"items": items})

def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    submitted = False
    if request.method == "POST":
        form = DeliveryOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.item = item
            order.item_id = item_id
            order.save()
            # form.save()
            return HttpResponseRedirect('/item/' + item_id +'/?submitted=True')
    else:
        form = DeliveryOrderForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'items/item_detail.html', {"item": item, "submitted": submitted, "form": form})

def create_item(request):
    submitted = False
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            #form.save()
            return HttpResponseRedirect('/create-item?submitted=True')
    else:
        form = ItemForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'items/create_item.html', {"form": form, "submitted": submitted})


def delete_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('item-list')






# Manager System
def approve_order(request):
    orders = DeliveryOrder.objects.all()
    return render(request, "items/approve_order.html", {"orders": orders})


def verified(request, deliveryorder_id):
    order = DeliveryOrder.objects.get(pk=deliveryorder_id)
    order.is_verified = True
    order.save()
    return redirect('approve-order')

def unverified(request, deliveryorder_id):
    order = DeliveryOrder.objects.get(pk=deliveryorder_id)
    order.is_verified = False
    order.save()
    return redirect('approve-order')

def approved(request, deliveryorder_id):
    order = DeliveryOrder.objects.get(pk=deliveryorder_id)
    order.is_approved = True
    order.save()
    return redirect('approve-order')

def disapproved(request, deliveryorder_id):
    order = DeliveryOrder.objects.get(pk=deliveryorder_id)
    order.is_approved = False
    order.save()
    return redirect('approve-order')

def cancel(request, deliveryorder_id):
    order = DeliveryOrder.objects.get(pk=deliveryorder_id)
    order.is_canceled = True
    order.save()
    return redirect('approve-order')


#Courier System
def delivery_order(request):
    orders = DeliveryOrder.objects.all()
    return render(request, "items/delivery_order.html", {"orders": orders})


def completed(request, deliveryorder_id):
    order = DeliveryOrder.objects.get(pk=deliveryorder_id)
    order.is_completed = True
    order.save()
    return redirect('delivery-order')

def notcompleted(request, deliveryorder_id):
    order = DeliveryOrder.objects.get(pk=deliveryorder_id)
    order.is_completed = False
    order.save()
    return redirect('delivery-order')


#Finance Office system
def finance_office(request):
    orders = DeliveryOrder.objects.all()
    return render(request, "items/finance_office.html", {"orders": orders})

def edit_invoice(request, invoice_id):
    order = DeliveryOrder.objects.get(pk=invoice_id)
    form = InvoiceForm(request.POST or None, instance=order)
    if form.is_valid():
        tax_service = order.item.price * order.quantity / 100 * (order.tax + order.service)
        order.invoice = order.item.price * order.quantity + tax_service
        order.is_invoice = True
        form.save()
        return redirect('finance-office')

    return render(request, 'items/create_invoice.html', {"order": order, "form": form})


def invoice_detail(request, invoice_id):
    invoice = DeliveryOrder.objects.get(pk=invoice_id)
    return render(request, 'items/invoice_detail.html', {"invoice": invoice})
