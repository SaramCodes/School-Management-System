from django import forms
from .models import User
from klass.models import Klasses
from django.core.validators import ValidationError
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given Email and
    password.
    """
    error_messages = {
        'password_mismatch': _("Passwords don't match!"),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'validate'}),
        help_text= _("Your password should be longer than 8 characters and make sure it is a strong one. It can't be entirely numeric"),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'validate'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    part_of = forms.ModelChoiceField(queryset=Klasses.objects.all(), empty_label="Please select a class if the user being added is a student or teacher", required=False)

    date_of_birth = forms.DateField(help_text="Please enter the date in yyyy-mm-dd format or otherwise the form will throw an error.", required=False)

    image = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "date_of_birth", "bio", "address", "phone_number", "is_student", "is_teacher", "is_admin", "image")

        # widgets = {
        #     "email" : forms.EmailInput(attrs={'class':'validate'}),
        #     "bio" : forms.Textarea(attrs={'class':'materialize-textarea'}),
        #     "is_admin": forms.CheckboxInput(attrs={'class':'filled-in-box'}),
        #     "first_name":forms.TextInput(attrs={'class':'validate'}),
        #     # "date_of_birth":forms.TextInput(attrs={'class':'datepicker'}
        # }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=225)
    password = forms.CharField(
    label=("Password"),
    strip=False,
    widget=forms.PasswordInput
    )

    error_messages = {
        'invalid_login':(
            "Please enter a correct email and password. Note that both "
            "fields may be case-sensitive.")
    }


class UserUpdateForm(forms.ModelForm):

    date_of_birth = forms.DateField(help_text="Please enter the date in yyyy-mm-dd format or otherwise the form will throw an error.", required=False)

    image = forms.ImageField(required=False)

    part_of = forms.ModelChoiceField(queryset=Klasses.objects.all(), empty_label="Please select a class if the user being added is a student or teacher", required=False)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "date_of_birth", "bio", "address", "phone_number", "is_student", "is_teacher", "is_admin", "part_of", "image")

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    # def check_teacher(self):
    #     klass = self.cleaned_data.get("part_of")
    #     if self.cleaned_data['is_teacher'] == True and klass.partof.filter(is_teacher=True).exists():
    #         raise ValidationError("A teacher is already in this class. Choose another class.")
    #     return klass




    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class SteacherUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(help_text="Please enter the date in yyyy-mm-dd format or otherwise the form will throw an error.", required=False)

    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ("date_of_birth", "bio", "address", "phone_number", "image")

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     try:
    #         w,h = get_image_dimensions(image)
    #         if w != h:
    #             raise ValidationError("Please upload an image with equal height and width dimenstions so it is a complete square")
    #     except AttributeError:
    #         pass
    #
    #     return image
