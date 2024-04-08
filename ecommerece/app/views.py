from django.shortcuts import render
from rest_framework.views import APIView
from .models import Customer, Product, Cart, OrderPlaced
from django.db.models import Q


class ProductAPiView(APIView):

    def get(self,request):

        queryset= Product.objects.filter(Q(category='TW') | Q(category='BW') | 
                                                                  Q(category='M') | Q(category='L')).values()
        topwear = queryset.filter(category='TW')
        bottomwear = queryset.filter(category='BW')
        mobile = queryset.filter(category='M')
        laptop = queryset.filter(category='L')
        return render(request, 'app/home.html', {'topwear':topwear, 'bottomwear':bottomwear, 'mobile':mobile, 'laptop':laptop})
        
class ProductDetail(APIView):
    
        def get(self,request,pk):
            product = Product.objects.get(pk=pk)
            return render(request, 'app/productdetail.html', {'product':product})

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
