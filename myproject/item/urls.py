from django.urls import path
from . import views

urlpatterns = [
    #Salesman system
    path("menu/", views.menu, name="menu"),
    path("item/<item_id>/", views.item_detail, name="item-detail"),
    path("create-item/", views.create_item, name="create-item"),
    path("item/delete/<item_id>/", views.delete_item, name="delete-item"),



    #Manager system
    path("approve-order/", views.approve_order, name="approve-order"),

    path("verified/<deliveryorder_id>/", views.verified, name="verified"),
    path("unverified/<deliveryorder_id>/", views.unverified, name="unverified"),
    path("approved/<deliveryorder_id>/", views.approved, name="approved"),
    path("disapproved/<deliveryorder_id>/", views.disapproved, name="disapproved"),
    path("cancel/<deliveryorder_id>/", views.cancel, name="cancel"),

    #Courier sytem
    path("delivery-order/", views.delivery_order, name="delivery-order"),

    path("completed/<deliveryorder_id>/", views.completed, name="completed"),
    path("notcompleted/<deliveryorder_id>/", views.notcompleted, name="notcompleted"),

    #Finance officer system
    path("finance-office/", views.finance_office, name="finance-office"),
    path("edit-invoice/<invoice_id>/", views.edit_invoice, name="edit-invoice"),
    path("invoice/<invoice_id>/", views.invoice_detail, name="invoice-detail"),
]
