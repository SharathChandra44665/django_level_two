from django.db import models

# Create your models here.
#
class TopicRead(models.Model):
    topic_name=models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):

    """docstring for  Web_page."""

    topic=models.ForeignKey(TopicRead,on_delete=models.CASCADE,)
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class  AccessRecord(models.Model):
    access_name=models.CharField(max_length=200)
    date=models.DateField()

    def __str__(self):
        return str(self.date)
