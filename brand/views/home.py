from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from brand.models.product import Product
from brand.models.category import Category
from brand.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.views import View

class Index(View):
    def get(self,request):
        cart= request.session.get('cart')
        print("CART GET: ", cart)
        if not cart:
            request.session['cart']={}
            
        categories=Category.all_category()
        c_id=request.GET.get('category')
        if c_id:
            products=Product.all_products_by_Category_id(c_id)
        else:
            products=Product.all_products()

        a = sum(request.session['cart'].values())
       
        print("CART: ",request.session['cart'])
        print("CART VALUES: ",request.session['cart'].values())

        mehr={'allproducts':products, 'categories':categories, 'cart':a}
        return render(request,'index.html',mehr)
        

    def post(self,request):
       products_id=request.POST.get('products_id')  
       remove=request.POST.get('remove')
       cart=request.session.get('cart')
       print("cart: ", cart)
       if cart:
            id_in_cart=cart.get(products_id)
            if id_in_cart:
                if remove:
                    if id_in_cart<=1:
                        cart.pop(products_id)
                    else:
                        cart[products_id] = id_in_cart - 1
                else:
                    cart[products_id] = id_in_cart + 1
                # print('id_in_cart: ', id_in_cart)
            else:
                cart[products_id]=1
       else:
            cart={}
            cart[products_id]=1
        
       request.session['cart']=cart
       print("product id:", products_id)
      
       return HttpResponseRedirect(reverse('index'))

