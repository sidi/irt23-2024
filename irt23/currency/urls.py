from django.urls import path

from . import views

urlpatterns = []

urlpatterns += [
    path('', views.home, name='home_page'),
]
urlpatterns += [
    path('department/', views.DepartmentList.as_view(), name='department_list'),
    path('department/add', views.DepartmentCreate.as_view(), name='department_create'),
    path('department/<slug:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    path('department/update/<slug:pk>', views.DepartmentUpdate.as_view(), name='department_update'),
    path('department/delete/<slug:pk>', views.DepartmentDelete.as_view(), name='department_delete')
]

urlpatterns += [
    path('student/', views.StudentList.as_view(), name='student_list'),
    path('student/add', views.StudentCreate.as_view(), name='student_create'),
    path('student/<slug:pk>', views.StudentDetail.as_view(), name='student_detail'),
    path('student/update/<slug:pk>', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<slug:pk>', views.StudentDelete.as_view(), name='student_delete')
]

urlpatterns += [
    path('import/department', views.import_departement_csv, name='department_import'),
]
