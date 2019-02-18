from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Classroom(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    subject = models.CharField(max_length=120)
    year = models.IntegerField()

    def get_absolute_url(self):
        return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    exam_grade =models.DecimalField(max_digits=6, decimal_places=2)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE,related_name='student') 

    def __str__(self):
        return self.name
    
