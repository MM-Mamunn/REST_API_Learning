from django.db import models

# Create your models here.
class database(models.Model):
    teacher_name= models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_duration = models.IntegerField()
    seat= models.IntegerField()