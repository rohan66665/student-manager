from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "course")

    
admin.site.site_header = "Student Manager Admin"
admin.site.site_title = "Student Manager"
admin.site.index_title = "Welcome to Student Manager Dashboard"