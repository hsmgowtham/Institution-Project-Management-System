from django.db import models

# Create your models here.
class Instituition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Instituition'