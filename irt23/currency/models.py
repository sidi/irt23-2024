from django.db import models


class Department(models.Model):
    code = models.CharField(max_length=3, unique=True)
    label = models.CharField(max_length=255)
    def __str__(self):
        return str(self.code) + ' --- ' + str(self.label)

class Student(models.Model):
    matricule = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    departement = models.ForeignKey(Department, on_delete=models.CASCADE)


    