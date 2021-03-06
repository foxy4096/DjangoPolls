from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    """
    A model to add question
    """
    question_text = models.CharField(max_length=255)
    voted = models.ManyToManyField(User, related_name='voted_users')
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')

    def __str__(self):
        """
        Sting representation of the choice
        """
        return self.question_text

class Choice(models.Model):
    """
    A model to add choice on the question
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Sting representation of the choice
        """
        return self.choice_text