from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from shop.models import Produit
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)  
    email = models.EmailField(max_length=254, null=True)
    profile_pic = models.ImageField(upload_to='user-pic', null=True, blank=True, default='images/usericon.png')
    
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)
    

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
    

    


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Customer_orderItem', null=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='Product', null=True)
    quantity= models.PositiveIntegerField(default=1, null=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True) 
    
    @property
    def get_total_price(self):
        return self.produit.prix * self.quantity   
    
    
    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
    
    def __str__(self):
        return self.produit.nom

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Customer_order', null=True)
    complete = models.BooleanField(default=False, null=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    produits = models.ManyToManyField(OrderItem)
    

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")
    
    def __str__(self):
        return self.customer.user.username





