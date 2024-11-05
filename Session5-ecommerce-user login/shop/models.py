from django.db import models

# Create your models here.

## black-coffee-ethiopia

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="uploadedimages", null=True, blank=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} - {self.description[:10]}" 
    
    @property
    def short_description(self):
        return self.description[:10]