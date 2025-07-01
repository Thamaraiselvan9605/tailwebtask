from django.db import models

class StudentsData(models.Model):
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
    marks = models.IntegerField()
