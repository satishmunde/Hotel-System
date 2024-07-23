from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Adjust max_digits and decimal_places as per your needs
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)  # Requires Pillow package for image handling

    def __str__(self):
        return self.name
