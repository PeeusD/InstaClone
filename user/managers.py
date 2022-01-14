from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy
 
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password ,  **extra_fields):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError(ugettext_lazy('Users must have an email address')) #getting error-msg in any language
        
        email = self.normalize_email(email) # .normalize_email() auto-converts capitalized email[e.g. Gmail.com] to small letters
        user = self.model(email=email, username=username, **extra_fields)
        
        user.set_password(password) #django adds sha algo with salting mechanism for saving password 
        user.save()
        return user
    
    
    #modifying bulilt-in SUPERUSER fields
    def create_superuser(self, email,  username, password, **extra_fields):
       
        """
        Creates and saves a superuser with the given email, username & password. 
        Here, create_superuser() is inheriting the create_user() method.
        """
        # changing the fields 'is active', 'is staff', 'superuser' fields set to true if not exists...
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_superuser=True'))

        user = self.create_user(email,  password, username, **extra_fields)
        return user
