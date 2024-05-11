from rest_framework import serializers
from django import forms
from .models import Project
from course.models import Course

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "pk",
            "name",
            "url",
            "course",
            "student",
            "instituition",
        ]
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields['course'].queryset = Course.objects.none()