from django.db import models


class Member(models.Model):
  f_name  = models.CharField(max_length=30)
  l_name  = models.CharField(max_length=30)
  email   = models.EmailField(max_length=70)
  contact = models.IntegerField()
  course  = models.CharField(max_length=30, null=True)
  flag    = models.CharField(max_length=20)
  
class Pertner(models.Model):
  name      = models.CharField(max_length=20)
  thumbnail = models.ImageField(upload_to="/temp")
  
class Staff(models.Model):
  f_name   = models.CharField(max_length=30)
  l_name   = models.CharField(max_length=30)
  position = models.CharField(max_length=30)
  contact  = models.IntegerField()

class News_letter(models.Model):
  e_mail = models.EmailField(max_length=70)
