import random
from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from classroom.models import ClassroomTeacher, Classroom
from students.models import Teacher


class Command(BaseCommand):
    help = 'Populates ClassroomStudent table with test data'

    def handle(self, *args, **options):
        fake = Faker()

        teachers = Teacher.objects.all()
        teacher = random.choice(teachers)
        classroom = Classroom.objects.all()[0]

        for _ in range(30):
            classroom_teacher = ClassroomTeacher.objects.create(
                teacher=teacher,
                classroom=classroom
            )
            classroom_teacher.save()


