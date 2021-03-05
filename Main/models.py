from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title
