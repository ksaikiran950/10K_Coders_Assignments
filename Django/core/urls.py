from django.urls import path
from .views import Home,Add_Student
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add_student/',Add_Student.as_view(),name='add_student'),
]
