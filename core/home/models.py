from django.db import models
import uuid

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name

class College(models.Model):
    college_name = models.CharField(max_length=200)

    def __str__(self):
        return self.college_name


class Student(models.Model):
    college = models.OneToOneField(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=100,
        choices=(("Female", "Female"), ("Male", "Male")),
        default="Male"
    )
    phone_number = models.CharField(max_length=10)
    student_bio = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)
    student_registeration = models.DateTimeField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)       
    slug = models.SlugField(unique=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


