from django.db import models



class ProductQuerySet(models.QuerySet):
    def soft_delete(self):
        return self.update(is_deleted=True)
    
    def restore(self):
        return self.update(is_deleted=False)

    def hard_delete(self):
        return self.delete()

    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)
