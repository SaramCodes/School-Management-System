from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from klass.models import Klasses
from django.core.urlresolvers import reverse

# from klass.models import GroupOfStudents
class StudentManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(StudentManager, self).filter(is_student=True)


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    bio = models.TextField(blank=True, help_text='write something about yourself...')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, help_text="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.") # validators should be a list
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    address = models.CharField(max_length=225, blank=True)
    part_of = models.ForeignKey(Klasses, null=True, blank=True, related_name="partof", on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="profile_pictures", blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('user_delete', kwargs={'id':self.id})

    def get_update_url(self):
        return reverse('user_update_view', kwargs={'id':self.id})

    def get_steacher_update_url(self):
        return reverse('steacher_update', kwargs={'id':self.id})

    #This one is for GRADES
    def get_grade_create_url(self):
        return reverse('grade-create', kwargs={'id':self.id})





    #This is for GRADES ABOVE END





    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
