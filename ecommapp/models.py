from django.db import models

# Create your models here.]

class Categories(models.Model):
    Category_name=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Category_name
    
class Products(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    Category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    price=models.PositiveBigIntegerField()
    Image=models.ImageField(upload_to="images",null=True)
    description=models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.product_name