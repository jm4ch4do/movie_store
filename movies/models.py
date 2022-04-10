from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=200)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    last_modified = models.DateField(auto_now=True)
    published = models.DateField(blank=True, null=True, default=None)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title
