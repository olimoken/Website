from django.db import models
# Create your models here.


class Zapal(models.Model):
    ism = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.ism