from django.db import models

# Create your models here.
class Question(models.Model):
  question = models.TextField(null = True)
  question_no = models.IntegerField(null = True)

  def __str__(self):
    return self.question

class Option(models.Model):
  option = models.TextField(null = True)
  question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name="option")
  answer = models.BooleanField(default = False)

  def __str__(self):
    return str(self.option)[:50] + " --> " + str(self.question.question)[:20]