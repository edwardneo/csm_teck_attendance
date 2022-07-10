from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('sections/', views.sections),
    path('sections/<int:section_id>/students/', views.section_students),
    path('sections/<int:section_id>/details/', views.section_details),
    path('students/<int:student_id>/details/', views.student_details),
    path('students/<int:student_id>/attendances/', views.student_attendances),
]