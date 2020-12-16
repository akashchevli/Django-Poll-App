from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    by_publishe = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.question
    class Meta:
        db_table = 'Questions'
        

class Answers(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return "{0}-{1}".format(self.question_id, self.answer)
    class Meta:
        db_table = 'Answers'
    

class Voting(models.Model):
    by_publishe = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}-{1}-{2}".format(self.question_id, self.answer_id, self.by_publishe)
    class Meta:
        db_table = 'Voting'

    



    

