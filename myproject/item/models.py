from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
#sharing entity


class Item(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    description = models.TextField(null=True, default=None, blank=True)


    def __str__(self):
        return self.name



class DeliveryOrder(models.Model):
    date_added_order = models.DateField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    home = models.CharField(max_length=30)

    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    is_invoice = models.BooleanField(default=False)
    is_invoice_created = models.BooleanField(default=False)
    service = models.IntegerField(default=10)
    tax = models.IntegerField(default=10)
    quantity = models.IntegerField(default=1)
    invoice = models.FloatField(default=0)

    def __str__(self):
        return f"Order for {self.item} for {self.user}"

    @property
    def Total(self):
        return self.order.invoice * self.order.quantity



