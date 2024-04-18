from django.db import models

class student_data(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'my_collection'

    def __str__(self):
        return self.name + " - " + self.email


def create_student(request, name, email):
    student = student_data(name=name, email=email)
    student.save()
    return student


def get_students():
    return student_data.objects.all()


def delete_student(id):
    student = student_data.objects.get(pk=id)
    student.delete()
    return student


def update_student(id, name, email):
    student = student_data.objects.get(pk=id)
    student.name = name
    student.email = email
    student.save()
    return student