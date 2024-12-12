from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    gpa = models.FloatField(default=0)
    classification = models.CharField(max_length=12,
                                      blank=True,
                                      null=True)
    is_test_entry = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    is_enrolled = models.BooleanField(default=False)
    is_test = models.BooleanField(default=False)

    """
    We need to add verification for address, city, state, zipcode.
    """

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = "Student"

    def calculate_gpa(self, grades):
        pass

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __iter__(self):
        for field in self._meta.fields:
            if field.name != "id" or field.name != "test":
                yield getattr(self, field.name)


class Staff(AbstractUser):

    degree = models.CharField(max_length=12,
                              blank=True,
                              null=True)
    university = models.CharField(max_length=100,
                                  blank=True,
                                  null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    office_number = models.CharField(max_length=10, blank=True, null=True)
    office_phone = models.CharField(max_length=14, blank=True, null=True)
    is_test_entry = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    is_test = models.BooleanField(default=False)


    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = "Student"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __iter__(self):
        for field in self._meta.fields:
            if field.name != "id":
                yield getattr(self, field.name)



class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=12)
    relationship = models.CharField(max_length=25)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_test_entry = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.first_name} {self.last_name} emergency contact for {self.student.first_name}"
                f"{self.student.last_name}")


class Demerit(models.Model):
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='demerits_given')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='demerits_received')
    incident_report = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_test_entry = models.BooleanField(default=False)

    def __str__(self):
        return (f"By {self.teacher.first_name} {self.teacher.last_name} given to "
                f"{self.student.first_name} {self.student.last_name}")


class MedicalInformation(models.Model):
    pass