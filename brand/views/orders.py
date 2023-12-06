from django.shortcuts import render
from django.views import View
from brand.models.order import Order
from brand.middlewares.auth import auth_middleware

class OrderView(View):

    def get(self,request):
        customer_id=request.session.get('customer')
        print("customerid: ", customer_id )
        order=Order.order_by_customer_id(customer_id)
        mehr={'orders': order}
        return render(request, 'order.html', mehr)
        