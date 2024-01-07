from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

from django.utils import timezone
# Create your models here.


#Custom User Manager

class UserManager(BaseUserManager):
    def create_user(self,email,phonenumber=None,password=None,**extra_fileds):
        if not email:
            raise ValueError("Email is required!")
        email=self.normalize_email(email)
        user=self.model(email=email,phonenumber=phonenumber,**extra_fileds)
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_superuser(self,email,password,phonenumber,**extra_fileds):
        if not phonenumber:
            raise ValueError("Phone Number Required!")
        user=self.create_user(email=email,phonenumber=phonenumber,password=password,**extra_fileds)
        user.is_superuser=True
        user.is_admin=True
        user.is_staff=True
        user.save(using=self.db)
        return user


#Custom User Model
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(verbose_name="Email",max_length=40,unique=True)
    phonenumber=models.CharField(verbose_name="Phone Number",max_length=10)
    bio=models.CharField(verbose_name="Bio",max_length=40,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profilepics/',null=True,blank=True)
    last_login=models.DateField(verbose_name="Lastlogin",default=timezone.now)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=True)
    is_user=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)


    USERNAME_FIELD="email"

    REQUIRED_FIELDS = ['phonenumber']

    objects=UserManager()

    def __str__(self):
        return self.email