from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE =(('Admin','ADMIN'),('Student','Student'),('Teacher','Teacher'))
    user_type= models.CharField(choices=USER_TYPE,max_length=10,blank=True)
    
    def __str__(self) -> str:
        return self.username
    
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,related_name='Profile', blank=True)

    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(blank=True,null=True)
    address = models.CharField(max_length=300)
    family_member_count = models.PositiveIntegerField(null=True, blank=True)