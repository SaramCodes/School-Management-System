from .models import Klasses
from django import forms
from accounts.models import User


class KlassesForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=User.objects.filter(part_of=None).filter(is_student=True), required=False, help_text="Add students")

    teacher = forms.ModelChoiceField(queryset=User.objects.filter(part_of=None).filter(is_teacher=True), required=False, empty_label="Choose a teacher for this class.")
    class Meta:
        model=Klasses
        fields =("name", "students", "teacher")

class KlassesUpdateForm(forms.ModelForm):
    class Meta:
        model=Klasses
        fields =("name",)
