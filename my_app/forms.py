from django.forms import ModelForm
from .models import *
class task_form(ModelForm):
    class Meta :
        model = guna
        fields = ["student_name","task_title","status","deadline","trainer_name","score"]