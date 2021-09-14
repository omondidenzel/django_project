from django.db import models

# Create your models here.
class Members(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    passwd = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + " " + self.lname