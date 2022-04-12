from django.db import models


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10)
    isbn_13 = models.CharField(max_length=13)


# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=200)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    last_modified = models.DateField(auto_now=True)
    is_published = models.DateField(blank=True, null=True, default=None)
    cover = models.ImageField(upload_to='covers/', blank=True)

    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Character(models.Model):

    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='authors')


