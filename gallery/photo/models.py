from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='img/%y')

    def __str__(self):
        return self.title
