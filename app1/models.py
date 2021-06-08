from django.db import models
from django.db.models.fields import AutoField

class User(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    aadhar_number=models.IntegerField(null=True) 
    address=models.CharField(max_length=30)
    

class Bank(models.Model):

    name = models.CharField(max_length=30)
    code=models.IntegerField()
    address=models.CharField(max_length=30)


class Branch(models.Model):

    name = models.CharField(max_length=30)
    branch_code=models.IntegerField()
    address=models.CharField(max_length=30)
    # relations 
    bank_id=models.ForeignKey('Bank',on_delete=models.CASCADE) # one to many relationship with bank


class Account(models.Model):
    accountType = models.CharField(max_length=30)
    account_number=models.IntegerField() # aut o increment
    balance=models.IntegerField()
    branch = models.ManyToManyField(Branch) #method-1 manytto many relationship
    default_account=models.BooleanField(default=False)
    user= models.ManyToManyField(User) #method-1 manytto many relationship with user
    


class Loan(models.Model):
    loanType = models.CharField(max_length=30)
    loan_rate=models.IntegerField()
    amount=models.IntegerField() 
    branch = models.ManyToManyField(Branch) #method-1 manytto many relationship
    user= models.ManyToManyField(User) #method-1 manytto many relationship with user
    

class Balance(models.Model):
    price=models.IntegerField()

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)