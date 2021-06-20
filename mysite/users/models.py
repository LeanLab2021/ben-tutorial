from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField('birthday')
    gender = models.CharField(choices=(('male', '男性'),('female', '女性')), max_length=10)