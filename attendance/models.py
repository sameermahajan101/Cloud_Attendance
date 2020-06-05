from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Students(models.Model):
    moodleID = models.IntegerField(null=True, unique=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=50)
    time_logged = models.DateTimeField(auto_now=True)

    # def __str__(self):
    # return self.student
