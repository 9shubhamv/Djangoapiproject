from django.shortcuts import render ,get_object_or_404
# from django.http import JsonResponse
from apiapp.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404
from rest_framework import mixins,generics,viewsets
# Create your views here.

# def student_view(request):
#     students = Student.objects.all()
#     students_list = list(students.values())
#     return JsonResponse(students_list,safe = False)
@api_view(["GET","POST"])
def student_view(request):
    if request.method == "GET":
        # get all the data from student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def studentdetail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # update
    elif request.method =="PUT":
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Employees(APIView):
#     def get(self,request):
#         employee = Employee.objects.all()
#         print(employee)
#         serializer = EmployeeSerializer(employee,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer = EmployeeSerializer(data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class EmployeesDetails(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk = pk)
#         except Employee.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer =EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
# mixins
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class EmployeesDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

"""

"""
# generics view
# class Employees(generics.ListAPIView,generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
# --------------------------------------------------

# pk based generic
# class EmployeesDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class =EmployeeSerializer

#     lookup_field = "pk" # lookup field based on what we want to search for data.

#               OR          
# generic to reterive , updating and deleting object using pk

class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class EmployeesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer
    lookup_field = "pk"
"""

# querysets
# class EmployeeViewset(viewsets.ViewSet):
#     def list(self,request):
#         querset = Employee.objects.all()
#         serializer = EmployeeSerializer(querset,many = True)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def retrieve(self,request,pk=None):
#         employee = get_object_or_404(Employee,pk = pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def update(self,request,pk = None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors)
#     def delete(self, request,pk):
#         employee = get_object_or_404(Employee,pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

