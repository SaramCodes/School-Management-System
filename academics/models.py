from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from klass.models import Klasses

def validate_is_lt_hundred(value):
    if value > 100 or value < 0:
        raise ValidationError('The marks should fall within 0 - 100')


# Create your models here.
class RollCall(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,on_delete=models.CASCADE)
    present = models.BooleanField(default=False, blank=False, null=False)
    date = models.DateField()


    def __str__(self):

        return 'Roll call of {} for date {}'.format(self.student.first_name, self.date)



class Subject(models.Model):
    name = models.CharField(max_length=225)
    klass = models.ManyToManyField(Klasses, related_name='subjects')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject-detail', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('subject-delete', kwargs={'id':self.id})

    def get_update_url(self):
        return reverse('subject-update', kwargs={'id':self.id})



class Semester(models.Model):
    name = models.CharField(max_length=225, help_text="Choose a name for this period of grades, Semester, yearly or monthly test. However it suits your needs the best")
    period_start = models.DateField(auto_now_add=False, auto_now=False)
    period_end = models.DateField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return self.name

    def get_associate_klass_url(self):
        return reverse('grade-klass-list', kwargs={'id':self.id})

class Grade(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, blank=False, null=True, related_name="grades")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=False,null=False )
    score = models.IntegerField(blank=False, null=False, validators=[validate_is_lt_hundred])




    def __str__(self):
        return self.student.first_name
