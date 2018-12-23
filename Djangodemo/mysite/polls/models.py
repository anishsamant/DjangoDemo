from django.db import models

# Create your models here.

#to let django know that question class is type model
class Question(models.Model):
    questionText = models.CharField(max_length=200) #stores question text
    pub_date = models.DateTimeField("date published") #stores publish date

    def __str__(self):
        return self.questionText

class Choice(models.Model):
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choiceText

