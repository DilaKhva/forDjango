from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=50)
    desc = models.TextField()
    duration_months = models.IntegerField()
    def __str__(self):
        return self.title

class Lesson(models.Model):
    lesson_number = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    homework = models.TextField()
    theme = models.CharField(max_length=50)
    def __str__(self):
        return self.theme
