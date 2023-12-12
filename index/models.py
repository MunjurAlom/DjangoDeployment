from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title

class Ourteam(models.Model):
    name = models.CharField(max_length=50, blank=False)
    role_as_a =models.CharField(max_length=200, blank=False)
    expertise = models.CharField(max_length= 200, blank=False)
    twitter_link = models.URLField()
    fb_link = models.URLField()
    insta_link = models.URLField()
    linkedin_link = models.URLField()
    image = models.ImageField(upload_to='ourteam/', blank=False)

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=50, blank=False)
    role_as_a =models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='testimonials/', blank=False)
    description = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return self.name

# class Client(models.Model):
#     name = models.CharField(max_length=50, blank=False)
#     link = models.URLField()
#     image = models.ImageField(upload_to='client/', blank=False)

#     def __str__(self):
#         return self.name