from django.db import models
import datetime
import os
def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename="%s%s"%(now_time,filename) #this is the new file name for the uploaded file (automatically gives according to time)
    return os.path.join("upload/",new_filename) #this is the path where the file will be uploaded

# Create your models here.
class category(models.Model):
    bname = models.CharField(max_length=100,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.CharField(max_length=100,null=False,blank=False)
    status=models.BooleanField(default=True,help_text="0-default,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.bname
    
class Product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    bname = models.CharField(max_length=100,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    org_price=models.IntegerField(null=False,blank=False)
    sel_price=models.IntegerField(null=False,blank=False)
    description=models.CharField(max_length=100,null=False,blank=False)
    status=models.BooleanField(default=True,help_text="0-default,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.bname