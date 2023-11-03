from django.db import models

# Create your models here.



class UniveristyCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default=0, blank=True, null=False)

    object = models.Manager()

    # displays the object output values in form of a string

    def __str__(self):
        # returns the input value of the title and instructor name
        # field as a tuple to diplay in the browser instead of default
        display_course = '{0.campus_name}: {0.state}'
        return display_course.format(self)


    class Meta:
        verbose_name_plural = "University Campus"