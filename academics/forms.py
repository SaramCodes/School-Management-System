from django import forms
from .models import Subject, Grade, Semester
from klass.models import Klasses
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import validate_is_lt_hundred


class SubjectForm(forms.ModelForm):
    klass = forms.ModelMultipleChoiceField(queryset=Klasses.objects.all(), required=False, help_text="Add Subject to following classes...or not")

    class Meta:
        model = Subject
        fields = ("name", "klass",)


class GradeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.klass = kwargs.pop('klass', None)
        super(GradeForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = self.klass.subjects.all()
        self.fields['subject'].empty_label = "Select a subject from drop down"
        self.fields['score'].validators = [validate_is_lt_hundred]

    class Meta:
        model = Grade
        fields = ("subject", "score",)

class SemesterForm(forms.ModelForm):
    name = forms.CharField(max_length=225, required=True)
    class Meta:
        model=Semester
        fields = ("name", "period_start", "period_end")
