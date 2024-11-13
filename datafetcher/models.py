from django.db import models

# Create your models here.
class Fetch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_fetched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['date_fetched']
