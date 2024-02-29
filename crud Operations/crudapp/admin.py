# admin.py
from django.contrib import admin
from .models import Lecturer, Course

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "educational_background"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
