from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import product,category,Cart,signup,User_Signup,Contact,Order
from django.contrib.sessions.models import Session  
import stripe
import time

# Create your views here.
stripe.api_key='sk_test_QhSeKSq3sLTxE0VIwmsh1K9o00cU4DXYYq'
def index(request):
    navdata=category.objects.all()
    allProds = product.objects.all().order_by('-pid')
    return render(request,'home.html',{'product':allProds,'navbar':navdata})
def allproduct(request):
    navdata=category.objects.all()
    allProds = product.objects.all().order_by('-pid')
    return render(request,'allproduct.html',{'product':allProds,'navbar':navdata})


#Product view
def products(request,myid):

    navdata=category.objects.all()
    products= product.objects.filter(pid=myid)
    
    return render(request,'productview.html',{'product':products,'navbar':navdata})


# category list
def categories(request,cid):
    navdata=category.objects.all()
    products=product.objects.filter(category_id=cid)
    return render(request,'category.html',{'product':products,'navbar':navdata})


def cart(request):

     if request.session.has_key('is_loged'):
        cartcount=Cart.objects.filter(id= request.session['usercart'])[0]
        request.session['counter']= cartcount.products.count()
        cartsdata= Cart.objects.filter(id= request.session['usercart'])[0]
        
        navdata=category.objects.all()
        return render(request,'cart.html',{'cart':cartsdata,'navbar':navdata})
     else:
        return redirect('/')

def updatecart(request , proid):

    cart=Cart.objects.filter(id= request.session['usercart'])[0]
    pro=product.objects.get(pid=proid)
    if not pro in Cart.objects.filter(id= request.session['usercart']):
        cart.products.add(pro)
    
    new_cart= 0.00
    for item in cart.products.all():
        new_cart+= item.price
    cart.total=float(new_cart)
    cart.save()
    return redirect('/cart')


def removecart(request,cartid):
    cart= Cart.objects.filter(id= request.session['usercart'])[0]
    price= cart.products.get(pid=cartid)
    newprice=cart.total
    totalprice= newprice-price.price
    cart.total=totalprice
    cart.save()
    cart.products.remove(cartid)
    return redirect('/cart')

# Checkout view
def checkout(request):
    if request.method=="POST":
        x=int(request.POST['totalamount'])
        
        charge = stripe.Charge.create(
        amount=x*100,
        currency='usd',
        description='A Django charge',
        source=request.POST['stripeToken']
        )
        if(charge['paid']==True):

            order_id=str(time.time())
            Firstname=request.POST['Firstname']
            lastname=request.POST['lastname']
            phoneno=request.POST['phoneno']
            emailid=request.POST['emailid']
            address=request.POST['address']
            city=request.POST['city']
            district=request.POST['district']
            zipcode=request.POST['zipcode']
            userid=request.session['userid']
            tokenid=request.POST['stripeToken']
            totalamount=request.POST['totalamount']
            orderdata=Order(cart=Cart.objects.get(id=request.session['usercart']),Firstname=Firstname,lastname=lastname,phoneno=phoneno,emailid=emailid,address=address,city=city,district=district,zipcode=zipcode,userid=userid,tokenid=tokenid,totalamount=totalamount,order_id=order_id)
            
            orderdata.save()
            Thank=True
            message = "Your Payment is Sucessfull"
            return render(request,'home.html',{'msg':message,'Thank':Thank})
            
            
        
       
        
    cartsdata= Cart.objects.filter(id= request.session['usercart'])[0]
    return render(request,'checkout.html',{'data':cartsdata})
# Signup page
def signup(request):
    if request.method == 'POST':
        navdata=category.objects.all()
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
            
        data = User_Signup(fname=fname,lname=lname,email=email,password=password)
        data.save()
        message = "Your Account is Sucessfully created"
        userdata=User_Signup.objects.get(email=email)
        myid=userdata.sno
    
        mydata=Cart(user_id=myid)
        mydata.save()
        return render(request,'login.html',{'msg':message})  
        # return render(request,'isgnup.html')
    navdata=category.objects.all() 
    return render(request,'signup.html',{'navbar':navdata})

def login(request):
    if request.method == 'POST':
        
        email=request.POST['email']
        password=request.POST['password']
        data = User_Signup.objects.filter(email=email,password=password)
        if data:
           
            userdata= User_Signup.objects.get(email=email)
            cartdata=Cart.objects.get(user_id=userdata.sno)
            request.session['userid']=userdata.sno
            request.session['usercart']=cartdata.id
            cartcount=Cart.objects.filter(id= request.session['usercart'])[0]
            request.session['counter']= cartcount.products.count()
            request.session['is_loged'] = True
            allProds = product.objects.all()
            Thank = True
            message = "You are sucessfully login now you buy any items"
            
            return render(request,'home.html',{'msg':message,'Thank':Thank,'product':allProds})
        else:
            Thank = True
            message = "your detail is wrong check your name or a password"
            return render(request,'login.html',{'msg':message,'Thank':Thank})

  
    navdata=category.objects.all()  
    return render(request,'login.html',{'navbar':navdata})

def logout(request):
    if request.session.has_key('is_loged'):

        del request.session['is_loged']
        del request.session['counter']
        message = "you are Sucessfully Logout"
        Thank = True
        return render(request,'home.html',{"msg":message,"Thank":Thank})

    else:
        message = "you are Already logout"
        Thank = True
        return render(request,'login.html',{"msg":message,"Thank":Thank})

def contact(request):
    if request.method == 'POST':
        
        subject = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        data = Contact(name=name,email=email,phone=phone,content=subject)
        data.save()
        message = "your response is recorded"
        Thank = True 
        return render(request,'contact.html',{'msg':message,'Thank':Thank})
    navdata=category.objects.all()
    return render(request,'contact.html',{'navbar':navdata})

def tracker(request):
    navdata=category.objects.all()
    return render(request,'tracking.html',{'navbar':navdata})


def charge(request):
    if request.method == 'POST':
        x=int(request.POST['amount'])
           
        charge = stripe.Charge.create(
        amount=x*100,
        currency='usd',
        description='A Django charge',
        source=request.POST['stripeToken']
        )

        if(charge['paid']==True):
            payment = transictions(tuser_id=request.session['id'],tprice=x,tamout=222,token=request.POST['stripeToken'],status_id_id=0)
            payment.save()

            return HttpResponse('source')

def search(request):
    query = request.GET.get('search')
    
    data = product.objects.get(name__contains=query)
    
    navdata=category.objects.all()
    return render(request,'search.html',{'product':data,'navbar':navdata})
