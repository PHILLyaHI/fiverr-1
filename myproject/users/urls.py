from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path("myaccount/", views.myaccount, name="myaccount"),
    path("account/<user_id>/", views.account, name="account"),
]
