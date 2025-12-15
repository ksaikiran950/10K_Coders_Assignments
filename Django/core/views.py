from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Student
from .forms import AddStudentForm

class Home(View):
    def get(self,request):
        stu_data=Student.objects.all()
        return render(request,'core/home.html',{'stu_data':stu_data})
class Add_Student(View):
    def get(self,request):
        fm=AddStudentForm()
        return render(request,'core/add_student.html',{'form':fm})
    
    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/home')
        else:
            return render(request,'core/add_student.html',{'form':fm})
        

class Update(View):
    def post(self,request):
        pass



