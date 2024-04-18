from django.urls import path
from .views import api_overview, students_list, student_detail

urlpatterns = [
    # API Overview
    path('', api_overview, name='api_overview'),

    # Students List and Create
    path('students/', students_list, name='students_list'),
    # Student Detail, Update, and Delete
    path('students/<int:id>/', student_detail, name='student_detail'),

]