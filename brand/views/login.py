from django.shortcuts import render,redirect, HttpResponseRedirect
from brand.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.views import View

class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        print(request.GET.get('return_url'))
        return render(request,'login.html')
        
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.check_email(email)
        error_message=None

        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return HttpResponseRedirect(reverse('index'))
            else:
                error_message='''Email or Password Invalid!!!'''
        else:
            error_message='''Email or Password Invalid!!!'''
        return render(request,'login.html',{'error':error_message})

def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('login'))