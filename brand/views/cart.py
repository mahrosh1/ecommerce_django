from django.shortcuts import render,redirect
from brand.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.views import View
from brand.models.product import Product

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        mehr={'product_data': products}
        return render(request,'cart.html',mehr)
    