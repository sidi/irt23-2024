from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
# Create your views here.
class DepartmentList(ListView):
    model = Department

class DepartmentDetail(DetailView):
    model = Department  

class DepartmentCreate(CreateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('department_list')

class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('department_list')

class DepartmentUpdate(UpdateView):
    model =  Department
    fields = '__all__'
    success_url = reverse_lazy('department_list')

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student  

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model =  Student
    fields = '__all__'
    success_url = reverse_lazy('student_list')

def home(request):
    return render(request, 'home.html')