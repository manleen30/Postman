from django.db import models


class User(models.Model):
    fname=models.CharField(max_length=60)
    lname=models.CharField(max_length=60)
    def __str__(self):
        return self.fname

class Todo(models.Model):
    title=models.TextField(max_length=60)
    desp=models.TextField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    ANOTHER_CHOICES = (
    ('C','created'),
    ('P','inprocess'),
    ('D','done'),
    )
    
    status = models.CharField(max_length=1,choices=ANOTHER_CHOICES)

