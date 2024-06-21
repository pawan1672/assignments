from django.db import models
from .managers import ProductManager#To Integrate manager with the model
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    objects=ProductManager()
    all_objects = ProductManager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
        
    def restore(self, using=None, keep_parents=False):
        self.is_deleted = False
        self.save()

    def hard_delete(self):
        super(Product, self).delete()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
