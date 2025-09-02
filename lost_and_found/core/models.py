from django.db import models
from django.contrib.auth.models import AbstractUser


# 1. Department or Course (optional but good for future)
class Course(models.Model):
    name = models.CharField(max_length=100)   # e.g., "M.Sc Computer Science", "MCA"

    def __str__(self):
        return self.name


# 2. Year/Class (1st Year, 2nd Year, etc.)
class ClassRoom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.CharField(max_length=50)   # e.g., "1st Year", "2nd Year"

    def __str__(self):
        return f"{self.course.name} - {self.year}"


# 3. Valid Registration Numbers
class StudentRegistration(models.Model):
    reg_no = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reg_no} - {self.student_name}"


# 4. Custom User
class CustomUser(AbstractUser):
    reg_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.reg_no})"


# 5. Lost/Found Item
class Item(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    ITEM_TYPE = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE)
    date_reported = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    contact_info = models.CharField(max_length=100)

    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.title} ({self.item_type})"
