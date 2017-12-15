from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.
'''
Whenever you make changes to the models.py file you need to migrate the changes to the database.
Step 1:- python manage.py makemigrations
Step 2:- python manage.py migrate

'''
#The table name must be the class name

class profile(models.Model):
    name = models.CharField(max_length = 120)
    #descriptions = models.TextField(null=True) If null=True then no need to pass any value
    descriptions = models.TextField(default = 'default text value')

    def __unicode__(self):
        return self.name
