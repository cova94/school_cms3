import random
from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from classroom.models import ClassroomStudent, Classroom
from students.models import Student


class Command(BaseCommand):
    help = 'Populates ClassroomStudent table with test data'

    def handle(self, *args, **options):
        fake = Faker()

    counter = 0
    student = Student.objects.all()

    classroom = Classroom.objects.all()[0]

    for _ in range(30):
        classroom_student = ClassroomStudent.objects.create(
            student=student[counter],
            classroom=classroom
        )
        classroom_student.save()
        counter += 1

