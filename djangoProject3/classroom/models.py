from django.db import models
from students.models import Student, Staff
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Classroom(models.Model):
    name = models.CharField(max_length=75)
    class_code = models.CharField(max_length=10, blank=True, null=True)
    class_number = models.SmallIntegerField(blank=True, null=True)
    # syllabus
    # location
    # days
    # start_time
    max_seats = models.SmallIntegerField(default=0, blank=True, null=True)
    seats_taken = models.SmallIntegerField(default=0, blank=True, null=True)
    required_materials = models.TextField(blank=True, null=True)
    teachers = models.ManyToManyField(Staff,
                                     through='ClassroomTeacher',
                                     related_name='classrooms')
    students = models.ManyToManyField(Student,
                                      through='ClassroomStudent',
                                      related_name='classrooms')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)


    def calculate_final_grade(self):
        pass

    def __str__(self):
        return f"{self.name} {self.class_code}"


class ClassroomStudent(models.Model):
    student = models.ForeignKey(Student, related_name="classes", on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name="classroom_students", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.student} in {self.classroom}"


class ClassroomTeacher(models.Model):
    teacher = models.ForeignKey(Staff, related_name="classes", on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name="classroom_teachers", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} in {self.classroom}"






class Task(models.Model):
    TASK_TYPES = [
        ('assignment', 'Assignment'),
        ('project', 'Project'),
        ('quiz', 'Quiz'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    due_date = models.DateTimeField()
    created_by = models.ForeignKey(ClassroomTeacher, on_delete=models.CASCADE)  # Teacher or Staff
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Assignment(Task):
    max_score = models.IntegerField(default=100)
    instructions = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

class Project(Task):
    required_files = models.BooleanField(default=False)
    group_project = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Quiz(Task):
    number_of_questions = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    submitted_by = models.ForeignKey(ClassroomStudent, related_name='my_assignments',
                                     on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    points_scored = models.IntegerField(default=0)
    points_available = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    points = models.IntegerField(default=0)
    order = models.IntegerField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)