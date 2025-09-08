from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employee",views.EmployeeViewset,basename="employee")

urlpatterns = [
    path("student/",views.student_view),
    path("student/<int:pk>",views.studentdetail),

# class based
    # path("employee/",views.Employees.as_view()),
    # path("employee/<int:pk>",views.EmployeesDetails.as_view()),

# viewset
path("", include(router.urls))
]



