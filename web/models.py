from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=250)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE, default = "")
    def __str__(self):
        return "price {} ,{}".format(self.amount , self.date)
class Income(models.Model):
    text=models.CharField(max_length=200)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user= models.ForeignKey(User,null=False, on_delete=models.CASCADE, default = "")
    def __str__(self):
        return  "{} {}".format(self.date,self.amount)




