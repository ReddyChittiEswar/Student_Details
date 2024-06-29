from django.db import models
from django import forms

class Student(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    subject = models.CharField(max_length=64)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['name', 'age', 'subject']