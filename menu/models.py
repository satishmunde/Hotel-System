from django.db import models
from core.models import Company

class Category(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


from django.db import models
from django.core.files.storage import default_storage
from django.utils.deconstruct import deconstructible
import os

class MenuItem(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    availability = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    def save(self, *args, **kwargs):
        # Check if there is an old image and if it is different from the new one
        if self.pk:
            old_item = MenuItem.objects.get(pk=self.pk)
            if old_item.image and old_item.image != self.image:
                # Delete old image
                if default_storage.exists(old_item.image.path):
                    default_storage.delete(old_item.image.path)
        
        super().save(*args, **kwargs)
