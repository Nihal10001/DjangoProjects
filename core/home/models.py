from django.db import models
import uuid
from django.utils.text import slugify


class College(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="departments")

    def __str__(self):
        return f"{self.name} ({self.college.name})"


class Skills(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    college = models.OneToOneField(
        College, on_delete=models.CASCADE, related_name="college_student", null=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="department_students", null=True
    )
    skills = models.ManyToManyField(Skills)

    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=100,
        choices=(("Male", "Male"), ("Female", "Female")),
        default="Male"
    )
    phone_number = models.CharField(max_length=10)
    student_bio = models.TextField(editable=False)
    email = models.EmailField(null=True, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)

    slug = models.SlugField(unique=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# student = Student.objects.create(
#     college = "NSUT",
#     department = "Computer Science",
#     skills = "Taliking, Shying",
#     name = "Aditi",
#     age = 18,
#     gender = "Female",
#     phone_number = "9775896445",
#     student_bio = "I am gonna be an software engineer",
#     email = "aditi42@gmail.com",
#     dateofbirth = "2004-08-19"
# )
# college = ["DSU","IIT","NSU","DU"]
# departments = ["CS","Electrical","Mechanical"]

# class Student(models.Model):
#     department = models.ForeignKey(Department,
#                                    models.CASCADE,
#                                    models.SET_NULL,
#                                    models.SET_DEFAULT,
#                                    models.PROTECT)
    
#     department = models.OneToOneField(Department,
#                                    models.CASCADE,
#                                    models.SET_NULL,
#                                    models.SET_DEFAULT,
#                                    models.PROTECT)
    
#     department = models.ManyToManyField(Department)

    # student_registeration = models.DateTimeField(null=True, blank=True)
    # percentage = models.FloatField(default=10)
    # student_image = models.ImageField(upload_to= "image/student/")
    # file = models.FileField(upload_to= "file/student/")