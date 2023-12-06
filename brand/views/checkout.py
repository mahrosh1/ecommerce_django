from django.shortcuts import render,redirect
from brand.models.customer import Customer
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from brand.models.product import Product
from brand.models.order import Order

class CheckOut(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))

        for x in products:
            data_order= Order(customer=Customer(id=customer), product=x, price=x.price, address=address, phone=phone ,quantity=cart.get(str(x.id)))
            data_order.save()
        request.session['cart']={}
        return HttpResponseRedirect(reverse('cart'))