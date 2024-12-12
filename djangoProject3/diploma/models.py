from django.db import models
from django.contrib.auth.models import AbstractUser
from students.models import Student

class Transcript(models.Model):
    """
    Responsible for storing all information about students overall progress towards graduation.
    """
    graduation_date = models.DateField(null=True, blank=True)
    GPA = models.FloatField(default=0, null=True, blank=True)
    GPA2 = models.FloatField(default=0, null=True, blank=True)
    hours_attempted = models.IntegerField(null=True, blank=True)
    hours_completed = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

class StudentTranscript(Transcript):
    """
    Ties the Diploma model to a specific student.
    """
    student = models.OneToOneField(Student, related_name="my_transcripts", on_delete=models.CASCADE)

    def __str__(self):
        return f"Diploma for {self.student.first_name}{self.student.last_name}"


class Term(models.Model):
    """
    Contains information about classes being taken in a single term.
    """
    name = models.CharField(max_length=20)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    max_hours_allowed = models.IntegerField(default=20)
    gpa = models.FloatField(default=0, null=True)

class StudentTerm(Term):
    """
    This is responsible for tying a student object and a term object and will also have a hidden
    field for classroom objects for the term.
    """
    student_diploma = models.ForeignKey(StudentTranscript, related_name='terms_taken', on_delete=models.CASCADE,
                                        null=True, blank=True)

    def __str__(self):
        return f"{self.name} for {self.student_diploma.student.first_name} {self.student_diploma.student.last_name}"


class CoreClass(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=5)
    class_type = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField()
    credits = models.IntegerField()
    pre_requisites = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.department}{self.code}"


class ElectiveClass(CoreClass):
    is_elective = models.BooleanField(default=True)


class SpecialistClass(CoreClass):
    pass


class StudentCoreClass(CoreClass):
    student_transcript = models.ForeignKey(StudentTranscript, related_name='classes_taken', on_delete=models.CASCADE,
                                        null=True, blank=True)
    student_term = models.ForeignKey(StudentTerm, related_name='student_core_class', on_delete=models.CASCADE,
                                     null=True, blank=True)
    total_points_scored = models.IntegerField()
    total_points_available = models.IntegerField()
    calculated_grade = models.DecimalField(max_digits=5, decimal_places=4)
    letter_grade = models.CharField(max_length=2)

    def __str__(self):
        return (f"{self.name} {self.department}{self.code} for {self.student_transcript.student.first_name}"
                f"{self.student_transcript.student.last_name}")
