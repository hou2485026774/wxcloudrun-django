from datetime import datetime

from django.db import models


# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Counters'  # 数据库表名
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