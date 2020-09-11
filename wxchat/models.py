from django.db import models

import json

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)  #ID
    username = models.CharField(max_length=20, unique=True)
    headerimg = models.TextField()
    socketid = models.TextField(null=True)
    isonline = models.TextField(null=True)
    class Meta:
        db_table = 'wxchart_user'