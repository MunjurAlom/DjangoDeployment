from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50, blank=False)
    link = models.URLField()
    image = models.ImageField(upload_to='client/', blank=False)

    def __str__(self):
        return self.name