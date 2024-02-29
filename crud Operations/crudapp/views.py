# views.py
from django.shortcuts import render
from .models import Lecturer, Course
from django.contrib import messages

def index(request):
    lecturers = Lecturer.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":
        if "create_lecturer" in request.POST:
            name = request.POST.get("name_lecturer")
            edu_background = request.POST.get("edu_background")
            Lecturer.objects.create(
                name=name,
                educational_background=edu_background
            )
            messages.success(request, "Lecturer added successfully")

        elif "update_lecturer" in request.POST:
            id = request.POST.get("id_lecturer")
            name = request.POST.get("name_lecturer")
            edu_background = request.POST.get("edu_background")
            lecturer = Lecturer.objects.get(id=id)
            lecturer.name = name
            lecturer.educational_background = edu_background
            lecturer.save()
            messages.success(request, "Lecturer updated successfully")

        elif "delete_lecturer" in request.POST:
            id = request.POST.get("id_lecturer")
            Lecturer.objects.get(id=id).delete()
            messages.success(request, "Lecturer deleted successfully")

        elif "create_course" in request.POST:
            name = request.POST.get("name_course")
            Course.objects.create(name=name)
            messages.success(request, "Course added successfully")

        elif "update_course" in request.POST:
            id = request.POST.get("id_course")
            name = request.POST.get("name_course")
            course = Course.objects.get(id=id)
            course.name = name
            course.save()
            messages.success(request, "Course updated successfully")

        elif "delete_course" in request.POST:
            id = request.POST.get("id_course")
            Course.objects.get(id=id).delete()
            messages.success(request, "Course deleted successfully")

    context = {"lecturers": lecturers, "courses": courses}
    return render(request, "index.html", context=context)
