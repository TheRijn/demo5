from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ManyToManyField("Author", related_name="books")
    isbn = models.CharField(max_length=13)
    year = models.SmallIntegerField()


class Author(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateField()


class Review(models.Model):
    score = models.PositiveIntegerField()
    review_text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reviews')

# class book_author(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
