from django.db import models
from instituition.models import Instituition

# Create your models here.
class Course(models.Model):
    id = models.CharField(max_length=150, primary_key=True)
    name = models.CharField(max_length=150)
    instituition = models.ForeignKey(Instituition,db_column='instituition_id', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Course'