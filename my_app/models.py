from djongo import models

class guna(models. Model):
    student_name = models.CharField(max_length=100)
    task_title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    trainer_name = models.CharField(max_length=100)
    score = models.IntegerField()

# Create your models here.
