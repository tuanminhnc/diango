from django.db import models

# Create your models here.
class Question(models.Model):
    """
    Model class question
    """
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

class Choise(models.Model):
    """
    Model class choise quest
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=255)
    vote = models.IntegerField(default=0)