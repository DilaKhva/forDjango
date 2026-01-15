from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    choices = (
        ("excellent", "excellent"),
        ("good", "good"),
        ("bad", "bad"),)
    progress = models.CharField(max_length=10, choices=choices)
    is_absent = models.BooleanField(default=False)
    def __str__(self):
        return self.progress