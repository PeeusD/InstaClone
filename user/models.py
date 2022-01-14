from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]


class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank = True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    #removing built in fields in table.
    first_name =None
    last_name = None

    # optional fields
    bio = models.TextField(null=True, blank=True, help_text='Not more than 150 characters.')
    website = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    is_private_account = models.BooleanField(null=True, blank=True)
    
    #Change this constant (USERNAME FIELD) from email to 'username' for login ADMIN
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['full_name', 'username']
    objects = CustomUserManager()

    #Representing table records as a email as identifier 
    def __str__(self):
        return self.email


    @property  #counting people who follows current loggedin user...
    def follower_count(self):
        count = self.follow_followed.count()
        return count
    
    @property  #counting people whom -->the current logged user followed to...
    def following_count(self):
        count = self.follow_follower.count()
        return count
    
    @property
    def posts_count(self):
        count = self.post_set.count()
        return count

