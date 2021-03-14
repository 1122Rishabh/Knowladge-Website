from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)



class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")    
    phone=models.CharField(max_length=50,default="")    
    country=models.CharField(max_length=50,default="")    
    subject=models.CharField(max_length=500,default="")    


    def __str__(self):
        return self.name