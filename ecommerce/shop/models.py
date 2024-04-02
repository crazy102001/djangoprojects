from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='shop/images',null=True,blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='shop/images',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)   #only one time when we created a new record
    updated=models.DateTimeField(auto_now_add=True) #everytime when we update record
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




