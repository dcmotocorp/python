from django.shortcuts import render
from .models import *
from datetime import date
from django.db import transaction 
 # Create your views here.

def index(request):
    b1=Balance.objects.filter(price__gt=100)
    print(b1)
    return render(request,"index.html")


def forms(request):
    a1=Account.objects.get(id=6)
    print(a1.branch.all())
    return render(request,"forms.html")

@transaction.atomic
def submit_form(request):
    y=User(request.POST)
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    aadhar=request.POST['aadhar']
    address=request.POST['address']
    accounttype=request.POST['accounttype']
    balance=request.POST['balance']
    branch=request.POST['branch']
    with transaction.atomic():
        p1=User.objects.create(name=name,email=email,phone=phone,address=address,aadhar_number=aadhar)
        p1.save()
        a1=Account.objects.create(accountType=accounttype, account_number='1234567894',balance=balance)
        a1.save()
        a1.user.add(p1)
        a1.save()    
    return render(request,"forms.html")