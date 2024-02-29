# models.py
from django.db import models

class Lecturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Lecturer Name")
    educational_background = models.CharField(max_length=200, verbose_name="Educational Background")

    def __str__(self):
        return str(self.id)

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Course Name")

    def __str__(self):
        return str(self.id)
