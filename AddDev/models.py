from django.db import models

# Create your models here.

class Technology(models.Model) :
    name=models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class Domain(models.Model) :
    name=models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class Q_A(models.Model) :
    ques=models.FloatField()
    rating=models.FloatField()


class Blog(models.Model) :
    title=models.CharField(max_length=200)
    rating=models.FloatField()

    def __str__(self):
        return self.title


class Project(models.Model) :
    title=models.CharField(max_length=200)
    rating=models.FloatField()

    def __str__(self):
        return self.title


class Developer(models.Model) :
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    technology=models.ManyToManyField(Technology)
    domain=models.ManyToManyField(Domain)
    q_a=models.ManyToManyField(Q_A)
    blog=models.ManyToManyField(Blog)
    project=models.ManyToManyField(Project)
    score=models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name
