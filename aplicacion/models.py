# Required to assign User as a borrower
from django.contrib.auth.models import User
import uuid  # Required for unique book instances
from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User
from datetime import date

class Usuario(models.Model):
    username = models.CharField('username', max_length=100, unique=False, help_text='username')

    def __str__(self):
        return str(self.username)


class Tweet(models.Model):
    texto = models.CharField('texto', max_length=1000, unique=False, help_text='texto')
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(verbose_name='fecha', null=True, blank=True)

    def __str__(self):
        return str(self.usuario) + ' on ' + str(self.fecha)


class Retweet(models.Model):
    tweet = models.ForeignKey('Tweet', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    fechaDeRetweet = models.DateField(verbose_name='fechaDeRetweet', null=True, blank=True)

    def __str__(self):
        return str(self.tweet) + ' by ' + str(self.usuario)


"""
class Book(models.Model):
    #Model representing a book (but not a specific copy of a book).
    title = models.CharField('title', max_length=100, unique=False, help_text='help!')
    book_num = models.IntegerField()
    date_of_birth = models.DateField(verbose_name='Birth', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Write")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    friends = models.ManyToManyField("self")
    # in case I have to create a primary key specifically
    idd = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability')

    def __str__(self):
        #String for representing the Model object
        return self.title

    def get_absolute_url(self):
        #Returns the url to access a particular book instance.
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        ordering = ['title', 'author']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def display_genre(self):
        # Create a string for the Genre. This is required to display genre in Admin.
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
"""
