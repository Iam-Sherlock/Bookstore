from django.shortcuts import render,redirect,HttpResponse
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"shop/index.html")
def register(request):
    return render(request,"shop/reg.html")
def collection(request):
    Category = category.objects.filter(status=0)
    return render(request,"shop/collection.html",{ "Category":Category})
def collectionview(request,bname):
    if (category.objects.filter(bname=bname,status=0)):
        products=Product.objects.filter(category__bname=bname)
        return render(request,"shop/products/index.html",{ "products":products,"bname":bname})
    else:
        messages.warning(request,"No such Category Found")
        return redirect("categories")
    
def product_details(request,cname,pname):
    if(category.objects.filter(bname=cname,status=0)):
        if(Product.objects.filter(bname=pname,status=0)):
            product=Product.objects.filter(bname=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"product":product})
        else:
            messages.warning(request,"No such Product Found")
            return redirect("categories")
    else:
        messages.warning(request,"No such Category Found")
        return redirect("categories")