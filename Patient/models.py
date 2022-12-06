from django.db import models
from Doctor.models import Doctor

# Create your models here.
GENDER_CHOICES = (
    ("MALE", "male"),
    ("FEMALE", "female")
)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="MALE")
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    symtoms = models.TextField()
    presciption = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.patient.name + " - " + self.doctor.name

class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.patient.name + " - " + self.amount

class Test(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    test_name = models.CharField(max_length=100)
    test_description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.patient.name + " - " + self.test_name


class TestReport(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    report = models.TextField(default="No Report")

    def __str__(self):
        return self.test.patient.name + " - " + self.test.test_name

class Companion(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.patient.name + " - " + self.name

