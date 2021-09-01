from django.db import models


# Create your models here.
class Era(models.Model):
    name = models.CharField(max_length=100)


# Create your models here.
class Poet(models.Model):
    name = models.CharField(max_length=100)
    era = models.ForeignKey(Era, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']  # todo() this is costly


# Create your models here.
class Poem(models.Model):
    head = models.CharField(max_length=300, null=True)
    body = models.TextField(null=True)
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)

    class Meta:
        ordering = ['head']  # todo() this is costly
