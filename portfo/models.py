
# models.py
from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
