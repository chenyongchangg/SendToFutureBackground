from django.db import models
# Create your models here.




class Dto(models.Model):

    email = models.EmailField()
    date = models.DateTimeField()
    content = models.TextField()
    isPublic = models.BooleanField(default= True )
    isSend  = models.BooleanField(default=False)

