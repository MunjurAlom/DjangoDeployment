from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=700, blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=700, blank=False)
    

    def __str__(self):
        return self.subject