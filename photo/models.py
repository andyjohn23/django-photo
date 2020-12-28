from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=40)
    image = CloudinaryField('image')
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()