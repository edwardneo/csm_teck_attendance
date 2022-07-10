from django.contrib import admin

# Register your models here.
from .models import User, Student, Mentor, Section, Course, Attendance

admin.site.register(User)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "section", "course", "active", "banned"]
    list_editable = ["active", "banned"]

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "course"]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["id", "mentor", "capacity", "description"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    list_display = ["id", "student", "date", "presence"]