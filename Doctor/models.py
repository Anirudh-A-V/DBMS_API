from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ("MALE", "male"),
    ("FEMALE", "female")
)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="MALE")
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField()
    qualification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.qualification

class DutyTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    day = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    def __str__(self):
        return self.doctor.name + " " + self.day


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class DoctorDepartment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.doctor.name + " " + self.department.name
