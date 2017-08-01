from django.db import models
from .course_list import COURSE_CHOICES
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=1, choices=tuple((str(x), str(x)) for x in range(1,5)))
    course_name = models.CharField(max_length=50, choices=COURSE_CHOICES)
    course_number = models.IntegerField()
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.save()

    def __str__(self):
        return "Date: " + str(self.created_at.date()) + " " + self.name + " Year:" + str(self.year)
