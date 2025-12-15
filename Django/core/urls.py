from django.urls import path
from .views import Home,Add_Student,Update
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add_student/',Add_Student.as_view(),name='add_student'),
    path('update/<int:id>/',Update.as_view(),name="update_student"),
]
