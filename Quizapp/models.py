from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class QuesForm(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200, null=True)
    choice1 = models.CharField(max_length=200, null=True)
    choice2 = models.CharField(max_length=200, null=True)
    choice3 = models.CharField(max_length=200, null=True)
    choice4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    marks = models.IntegerField(default=2)

    def __str__(self):
        return self.question
