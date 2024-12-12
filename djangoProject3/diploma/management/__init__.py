from django.core.management.base import BaseCommand
from diploma.models import CoreClass
from diploma.class_library.class_index import CORE_CLASSES

class Command(BaseCommand):
    help = 'populates the Core Class db table'

