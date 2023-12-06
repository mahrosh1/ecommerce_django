from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    desc=models.CharField(max_length=200, default='', null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products/')
    

    @staticmethod
    def all_products():
        return Product.objects.all()    

    @staticmethod
    def all_products_by_Category_id(m):
        if m:
            return Product.objects.filter(category=m)
        else:
            return Product.allproducts()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    
    def __str__(self):
        return self.name