from django.db import models
from .daysOfWeek import DAYS_OF_WEEK

# Create your models here.



class Timepost(models.Model):
    student_username = models.CharField(max_length=100)
    tutor_pk = models.CharField(max_length=100)
    course_name = models.CharField(max_length=50)
    course_number = models.IntegerField()
    days = models.CharField(max_length = 10,choices = DAYS_OF_WEEK)
    start_time = models.TimeField(blank=False, null = False)
    end_time = models.TimeField(blank=False, null = False)

    def publish(self):
        self.save()

    def __str__(self):
        if self.userpk == -1:
            return "Invalid Post: Unknown User"
        timePost = Timepost.objects.get(pk=self.userpk)
        day = timePost.days
        start_time = timePost.start_time
        end_time = timePost.end_time
        return "On " + day + ", tutor starts from " + str(start_time) + " to " + str(end_time)