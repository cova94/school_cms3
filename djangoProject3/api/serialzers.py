from rest_framework import serializers
from students.models import Student, Teacher
from classroom.models import Classroom, ClassroomStudent, ClassroomTeacher, Grade, FinalGrade
from diploma.models import Diploma, StudentDiploma, Term, StudentTerm, CoreClass, StudentCoreClass, ElectiveClass

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassroomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomStudent
        fields = '__all__'

class ClassroomTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomTeacher
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class FinalGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalGrade
        fields = '__all__'

class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
