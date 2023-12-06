from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from brand.models.product import Product
from brand.models.category import Category
from brand.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.views import View


class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        phone=request.POST.get('phone')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        password=request.POST.get('password')
        email=request.POST.get('email')
        
        value={'firstname':fname,"lastname":lname,'phone':phone,'password':password,'email':email}
        error_message = None
        customer=Customer(first_name=fname,last_name=lname,phone=phone,email=email,password=password)
        error_message=self.validatecustomer(customer)

        if not (error_message):
            customer.password=make_password(customer.password)
            customer.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            data={'error':error_message,'values':value}
        return render(request,'signup.html',data)


    def validatecustomer(self,customer):
        error_message=None

        if not customer.first_name:
            error_message='''First Name Required!!!'''
        elif len(customer.first_name)<4:
            error_message='''First Name must be atleast of 4 chracters or more!'''
        elif not customer.last_name:
            error_message='''Last Name Required!!!'''
        elif len(customer.last_name)<4:
            error_message='''Last Name must be atleast of 4 chracters or more!'''
        elif not customer.phone:
            error_message='''Phone No Required!!!'''
        elif len(customer.phone)<11:
            error_message='''Phone No must be 10 characters.'''
        elif not customer.password:
            error_message='''Password Required!!!'''
        elif len(customer.password)<=4:
            error_message='''Password must be of altleast 10 chracters'''
        elif len(customer.email)<5:
            error_message='''Email must be 5 charcters long.'''
        elif customer.isExists():
            error_message='''Email Already Exists!!!'''
        else:
            pass
        return error_message