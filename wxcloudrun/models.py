from datetime import datetime

from django.db import models
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30,unique=True) #字符串
    spwd = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    #flag = models.CharField(max_length=255)
    #设置生成的表的信息
    class Meta:
        db_table = 'users'
class Img(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='img',null=False)