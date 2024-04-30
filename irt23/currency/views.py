from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

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

def import_departement_csv(request):

    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "Department", 'opath': "department"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        #code, label
        lines = file_data.split("\n")
        for line in lines:			
            fields = line.split(",")
            ob = Department()
            ob.code = fields[0]
            ob.label = fields[1]
            object_list.append(ob)
        
        Department.objects.bulk_create(object_list)

    except Exception as e:
        print("Error! Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("department_import"))

    return HttpResponseRedirect(reverse("department_list"))