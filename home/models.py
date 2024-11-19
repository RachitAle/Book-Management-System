from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    User = models.ForeignKey(User,on_delete= models.SET_NULL,blank=True,null=True)
    book_name = models.CharField(max_length=40)
    book_desc = models.TextField(null=True,blank=True)
    book_image = models.ImageField(upload_to = 'book_image',null=True,blank=True)
    
    def __str__(self):
        return(f'{self.book_name}')
    
  