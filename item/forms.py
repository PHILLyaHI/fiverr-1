from django import forms
from django.forms import ModelForm
from item.models import Item, DeliveryOrder

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "quantity", "description"]


class DeliveryOrderForm(ModelForm):
    class Meta:
        model = DeliveryOrder
        fields = ["quantity", "state", "city", "address", "home"]


class InvoiceForm(ModelForm):
    class Meta:
        model = DeliveryOrder
        fields = ["service", "tax", "quantity"]