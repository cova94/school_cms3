from diploma.class_library.class_index import CORE_CLASSES
from classroom import models
from diploma.models import CoreClass
from django.core.management.base import BaseCommand
from faker import Faker

class Command(BaseCommand):
    help = 'Populate CoreClass objects.'

    class_list = CORE_CLASSES


    def handle(self, *args, **options):
        fake = Faker()
        global CORE_CLASSES

        for department, classes in CORE_CLASSES['department'].items():
            for class_data in classes:
                core_class = CoreClass.objects.create(
                    name=class_data['name'],
                    department=department,
                    class_type=class_data['type'],
                    code=class_data['code'],
                    credits=class_data['credits'],
                    pre_requisites=class_data['pre_requisites']
                )
                core_class.save()

        self.stdout.write("Successfully populated core classes.")