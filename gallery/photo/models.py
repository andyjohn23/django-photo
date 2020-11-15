from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='img/%y')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title