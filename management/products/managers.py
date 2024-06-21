from django.db import models
from .querysets import ProductQuerySet



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
    
    def deleted(self):
        return self.get_queryset().deleted()
    
    def soft_delete(self):
        return self.get_queryset().soft_delete()
    
    def restore(self):
        return self.get_queryset().restore()
    
    def hard_delete(self):
        return self.get_queryset().hard_delete()
    
    def create_product(self, name, description, price):
        product = self.model(
            name=name,
            description=description,
            price=price
        )
        product.save(using=self._db)
        return product
