from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length = 50)
    picuture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = '')
    def __str__(self):
        return self.name