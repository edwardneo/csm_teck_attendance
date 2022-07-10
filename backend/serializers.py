from rest_framework import serializers

from backend.models import User, Student, Mentor, Section, Course, Attendance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name")


class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = Mentor
        fields = ("id", "user", "course")


class SectionSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer()

    class Meta:
        model = Section
        fields = ("id", "mentor", "capacity", "description")


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    section = SectionSerializer()
    course = CourseSerializer()

    class Meta:
        model = Student
        fields = ("id", "user", "section", "course", "active", "banned")

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("id", "date", "presence")