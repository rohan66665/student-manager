from django.shortcuts import render, redirect
from .models import Student

def index(request):
    return render(request, "students/home.html")

def add_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        course = request.POST["course"]
        Student.objects.create(name=name, age=age, course=course)
        return redirect("view_students")
    return render(request, "students/add_student.html")

def view_students(request):
    students = Student.objects.all()
    return render(request, "students/view_students.html", {"students": students})

def home(request):
    return render(request, "students/home.html")