from rest_framework import serializers
from apiapp.models import Student
from employee.models import Employee

# Student serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

# Employee serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"