from django.db import models
# Order CHoices
STATUS_CHOICES =(
        ("Started","Started"),
        ("Abandoned","Abandoned"),
        ("Finished","Finished"),
    )
# Create your models here.
class category(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname
    

class product(models.Model):
    pid= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    price= models.FloatField(max_length=1000,default=0.0)
    stock=models.IntegerField(default=0)
    description=models.TextField(max_length=1000,default="Dummay Description")
    image=models.ImageField(upload_to='uploads/',default='mypic')

class User_Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password=models.CharField(max_length=100)

class Cart(models.Model):
    products=models.ManyToManyField(product, null=True, blank=True)
    total=models.IntegerField(default=0)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    update=models.DateTimeField(auto_now_add=False, auto_now=True)
    active=models.BooleanField(default=True)
    user_id=models.IntegerField(default=0)
    
   
  
    
class signup(models.Model):
    sid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add = True , blank = True)

    def __str__(self):
        return self.name


# Order items
class Order(models.Model):
    order_id=models.CharField(max_length=200,default="Dummay", unique=True)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    status=models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")   
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    update=models.DateTimeField(auto_now_add=False, auto_now=True)
    Firstname=models.CharField(max_length=120 ,default="Dummay")
    lastname=models.CharField(max_length=120 ,default="Dummay")
    phoneno=models.CharField(max_length=120 ,default="Dummay")
    emailid=models.CharField(max_length=120 ,default="Dummay")
    address=models.CharField(max_length=120 ,default="Dummay")
    city=models.CharField(max_length=120 ,default="Dummay")
    district=models.CharField(max_length=120 ,default="Dummay")
    zipcode=models.CharField(max_length=120 ,default="Dummay")
    userid=models.CharField(max_length=120 ,default="Dummay")
    tokenid=models.CharField(max_length=120 ,default="Dummay")
    totalamount=models.FloatField(default=0.00)
    def __str__(self):
        return self.order_id
   
   
   