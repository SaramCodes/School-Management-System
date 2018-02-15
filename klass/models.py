from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse



class Klasses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('klasses_detail_view', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('klasses_delete_view', kwargs={'id':self.id})

    def get_update_url(self):
        return reverse('klasses_update_view', kwargs={'id':self.id})

    #THIS ONE IS FOR THE MODEL OF GRADE
    def get_grade_url(self):
        return reverse('grade-student-list', kwargs={'id':self.id})    
