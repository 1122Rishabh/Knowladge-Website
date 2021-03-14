from django.shortcuts import render
from.models import Product,Contact
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'shop/index.html')  
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        subject=request.POST.get('subject','')
        country=request.POST.get('country','')
        contact=Contact(name=name,email=email,phone=phone,country=country,subject=subject)
        contact.save()
    return render(request,"shop/contact.html")                        
def about(request):
    return render(request,"shop/about.html")
def php(request):
    return render(request,"shop/php.html")
def javascript(request):
    return render(request,"shop/javascript.html")
def C(request):
    return render(request,"shop/c.html")
def Cn(request):
    return render(request,"shop/cn.html")
def ml(request):
    return render(request,"shop/ml.html")
def ai(request):
    return render(request,"shop/ai.html")
def java(request):
    return render(request,"shop/java.html")
def python(request):
    return render(request,"shop/python.html")
def ide(request):
    return render(request,"shop/ide.html")
def javaide(request):
    return render(request,"shop/javaide.html")
def phpide(request):
    return render(request,"shop/phpide.html")
def javascriptide(request):
    return render(request,"shop/javascriptide.html")
def cide(request):
    return render(request,"shop/cide.html")
def cnide(request):
    return render(request,"shop/cnide.html")                    