from django.db import models
from instituition.models import Instituition
from course.models import Course
from student.models import Student

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    course = models.ForeignKey(Course,db_column='course_id', blank=True, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student,db_column='student_id', blank=True, null=True, on_delete=models.CASCADE)
    instituition = models.ForeignKey(Instituition,db_column='instituition_id', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Project'