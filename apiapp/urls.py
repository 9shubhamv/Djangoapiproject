from django.urls import path,include
from . import views
urlpatterns = [
    path("student/",views.student_view),
    path("student/<int:pk>",views.studentdetail),

# class based
    # path("employee/",views.Employees.as_view()),
    # path("employee/<int:pk>",views.EmployeesDetails.as_view()),
]
