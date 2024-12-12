import random
from faker import Faker
from students.models import Teacher, Student
from django.core.management.base import BaseCommand, CommandError
import sys

class Command(BaseCommand):
    help = "Populate teachers and students"


    def handle(self, *args, **options):
        self.stdout.write("Populating teachers and students")

        fake = Faker()
        UNIVERSITY_CHOICES = [
            "Harvard University",
            "Stanford University",
            "University of Alabama",
            "Massachusetts Institute of Technology (MIT)",
            "University of Cambridge",
            "University of Oxford",
            "California Institute of Technology (Caltech)",
            "Princeton University",
            "Yale University",
            "University of Chicago",
            "Columbia University",
            "University of California, Berkeley",
            "University of Toronto",
            "University of Michigan",
            "University of Tokyo",
            "Australian National University (ANU)",
            "University of Melbourne",
            "University of Sydney",
            "National University of Singapore (NUS)",
            "ETH Zurich (Swiss Federal Institute of Technology)",
            "Peking University",
            "Jacksonville State University",
            "Imperial College London",
            "University College London (UCL)",
            "University of Pennsylvania",
            "Duke University",
            "University of Edinburgh",
            "New York University (NYU)",
            "University of Washington",
            "University of Southern California (USC)",
            "University of British Columbia (UBC)",
        ]
        DEGREE_CHOICES = [
            "HSD",
            "BA",
            "MS",
            "PHD"
        ]
        CLASSIFICATION_CHOICES = [
            "FRESHMAN",
            "SOPHOMORE",
            "JUNIOR",
            "SENIOR",
        ]

        # create teacher objects for testing
        for _ in range(5):
            teacher = Teacher.objects.create(
                username=fake.unique.user_name(),
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name(),
                email=fake.unique.email(),
                password="test",
                is_test_entry=True,
                university=random.choice(UNIVERSITY_CHOICES),
                degree=random.choice(random.choice(DEGREE_CHOICES))
            )



        # create student objects for testing
        for _ in range(150):
            student = Student.objects.create(
                username=fake.unique.user_name(),
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name(),
                email=fake.unique.email(),
                password="test",
                is_test_entry=True,
                classification=random.choice(CLASSIFICATION_CHOICES)
            )
            student.save()