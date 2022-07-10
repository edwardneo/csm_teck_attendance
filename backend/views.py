from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from backend.models import User, Section, Student, Attendance
from backend.serializers import (
    AttendanceSerializer,
    UserSerializer,
    StudentSerializer,
    MentorSerializer,
    SectionSerializer,
    CourseSerializer,
)


@api_view(["GET"])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def sections(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT"])
def section_students(request, section_id):
    """
    GET: Return students in section
    PUT: Drop student
        - format: { "student_id": int }
    """
    if request.method == "GET":
        section = Section.objects.get(id=section_id)
        students = section.student_set.filter(active=True)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        student_id = request.data.get("student_id")
        student = Student.objects.get(id=student_id)
        student.active = False
        student.save()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def section_details(request, section_id):
    """
    GET: Return section details
    POST: Update section details
        - format: { "capacity": int, "description": str }
    """
    if request.method == "GET":
        section = Section.objects.get(id=section_id)
        serializer = SectionSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        section = Section.objects.get(id=section_id)
        capacity = request.data.get("capacity")
        description = request.data.get("description")
        if capacity is not None:
            section.capacity = capacity
        if description is not None:
            section.description = description
        section.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def student_details(request, student_id):
    """
    GET: Return student details
    """
    if request.method == "GET":
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "PUT"])
def student_attendances(request, student_id):
    """
    GET: Return student attendances
    PUT: Update attendance
        - format: { "attendance_id": int, "presence": str }
    """
    if request.method == "GET":
        attendances = Attendance.objects.filter(student__id=student_id)
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        attendance_id = request.data.get("attendance_id")
        presence = request.data.get("presence")
        attendance = Attendance.objects.get(id=attendance_id)
        attendance.presence = presence
        attendance.save()
        return Response(status=status.HTTP_200_OK)