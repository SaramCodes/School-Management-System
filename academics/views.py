from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
# My imports
from accounts.models import User
from .forms import SubjectForm, GradeForm, SemesterForm, RollCallForm
from .models import Subject, Grade, Semester
from klass.models import Klasses




#Everything relating subjects is here

def subject_list_view(request):
    if request.user.is_authenticated and request.user.is_admin:
        queryset = Subject.objects.all()

        template_name = "academics/subject/subjects_list_view.html"
        context = {
            "subject":queryset,
        }

        return render(request, template_name, context)
    else:
        raise Http404



def subject_create_view(request):
    # This checks if user is admin
    if request.user.is_authenticated and request.user.is_admin:
        #This checks if request is post and fills the form with data associated with that request
        if request.method == "POST":
            form = SubjectForm(request.POST)
            if form.is_valid():
                subject = form.save(commit=False)
                subject.save()
                form.save_m2m()

                messages.success(request, 'Subject Created SucessFully!!')
                return HttpResponseRedirect(subject.get_absolute_url())
        else:
            form = SubjectForm()
            return render(request, 'academics/subject/subjects_create_view.html', {'form': form})
    else:
        raise Http404



def subject_update_view(request, id):
    if request.user.is_authenticated and request.user.is_admin:
        instance = get_object_or_404(Subject, id=id)
        form = SubjectForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            messages.success(request, 'Subject Updated SucessFully!!')
            return HttpResponseRedirect(instance.get_absolute_url())

        else:
            return render(request, "academics/subject/subject_update_view.html", context = {
                "instance": instance,
                "form": form,
            })

    else:
        raise Http404

def subject_detail_view(request, id):
    # This checks if user is admin
    if request.user.is_authenticated and request.user.is_admin:

        subject = get_object_or_404(Subject, id=id)
        template_name = "academics/subject/subject_detail.html"
        context = {
            "subject":subject
        }
        return render(request, template_name, context)

    else:
        raise Http404


def subject_delete_view(request, id):
    if request.user.is_authenticated and request.user.is_admin:
        instance = get_object_or_404(Subject, id=id)
        instance.delete()
        messages.success(request, 'Subject Deleted Succesfully')
        return HttpResponseRedirect(reverse('subject-list'))
    else:
        raise Http404


# Everything relating subject is above

def semester_view(request):
    if request.user.is_authenticated:
        if request.user.is_admin or request.user.is_teacher:
            semester = Semester.objects.all()
            template_name = "academics/semester/semester_list.html"
            context = {"semester":semester,}
            return render(request, template_name, context)
        else:
            raise Http404
    else:
        raise Http404



def semester_create_view(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "POST":
            form = SemesterForm(request.POST)
            if form.is_valid():
                semester_boi = form.save(commit=False)
                semester_boi.save()
                messages.success(request, 'Semester Created SucessFully!!')
                return HttpResponseRedirect(reverse('semester-view'))
            else:
                messages.error(request, 'Correct the errors below')

        else:
            form = SemesterForm()
        return render(request, 'academics/semester/semester_create_view.html', {'form': form})
    else:
        raise Http404




def grade_klass_list_view(request, id):
    if request.user.is_authenticated and request.user.is_admin:
        semester = get_object_or_404(Semester, id=id)
        klasses = Klasses.objects.all()
        template_name = "academics/grade/grade_klass_list.html"
        context = {"klasses":klasses, "semester": semester}
        return render(request, template_name, context)
    else:
        raise Http404


def grade_student_list_view(request, semester_id, klass_id):
    if request.user.is_authenticated and request.user.is_admin:
        klass = get_object_or_404(Klasses, id=klass_id)
        semester = get_object_or_404(Semester, id=semester_id)
        students = klass.partof.filter(is_student=True)
        template_name = "academics/grade/grade_student_list.html"
        context = {
            "klass":klass,
            "students":students,
            'semester':semester
        }
        return render(request, template_name, context)
    else:
        raise Http404



def grade_view_for_teacher(request, semester_id, klass_id):
    if request.user.is_authenticated and request.user.is_teacher:
        klass = get_object_or_404(Klasses, id=klass_id)
        semester = get_object_or_404(Semester, id=semester_id)
        students = klass.partof.filter(is_student=True)
        template_name = "academics/grade/grade_student_list.html"
        context = {
            "klass":klass,
            "students":students,
            'semester':semester
        }
        return render(request, template_name, context)
    else:
        raise Http404



def grade_detail_view_teacher(request, semester_id, student_id):
    if request.user.is_authenticated and request.user.is_teacher:

        student = get_object_or_404(User, id=student_id)
        semester = get_object_or_404(Semester, id=semester_id)
        grades = semester.grades.filter(student=student)
        template_name = "academics/grade/grade_detail.html"
        context = {
            "student":student,
            "semester":semester,
            "grades":grades,
        }
        return render(request, template_name, context)

    else:
        raise Http404



def grade_detail_view(request, semester_id, student_id):
    if request.user.is_authenticated and request.user.is_admin:

        student = get_object_or_404(User, id=student_id)
        semester = get_object_or_404(Semester, id=semester_id)
        grades = semester.grades.filter(student=student)
        template_name = "academics/grade/grade_detail.html"
        context = {
            "student":student,
            "semester":semester,
            "grades":grades,
        }
        return render(request, template_name, context)

    else:
        raise Http404

def grade_create_view_teacher(request, student_id, semester_id):
    if request.user.is_authenticated and request.user.is_teacher:
        #This checks if request is post and fills the form with data associated with that request
        user = get_object_or_404(User, id=student_id)
        semester = get_object_or_404(Semester, id=semester_id)
        klass = user.part_of
        if request.method == "POST":
            form = GradeForm(request.POST, klass=klass)
            print(request.POST)

            if form.is_valid():
                grade = form.save(commit=False)
                print("almost there..")
                grade.student = user
                grade.semester = semester
                grade.save()
                print("works")
                messages.success(request, 'Grade Marked SucessFully!!')
                return HttpResponseRedirect(reverse('semester-view'))

            else:
                messages.error(request, 'Correct the errors below')
        else:
            form = GradeForm(klass=klass)

        context = {
            'form': form,
            'user':user,
            'klass':klass,
            }
        return render(request, 'academics/grade/grade_create_view.html', context )
    else:
        raise Http404




def grade_create_view(request, student_id, semester_id):
    if request.user.is_authenticated and request.user.is_admin:
        #This checks if request is post and fills the form with data associated with that request
        user = get_object_or_404(User, id=student_id)
        semester = get_object_or_404(Semester, id=semester_id)
        klass = user.part_of
        if request.method == "POST":
            form = GradeForm(request.POST, klass=klass)
            print(request.POST)

            if form.is_valid():
                grade = form.save(commit=False)
                print("almost there..")
                grade.student = user
                grade.semester = semester
                grade.save()
                print("works")
                messages.success(request, 'Grade Marked SucessFully!!')
                return HttpResponseRedirect(reverse('semester-view'))

            else:
                messages.error(request, 'Correct the errors below')
        else:
            form = GradeForm(klass=klass)

        context = {
            'form': form,
            'user':user,
            'klass':klass,
            }
        return render(request, 'academics/grade/grade_create_view.html', context )
    else:
        raise Http404

#Everythin relating Grades is above:



#Everything relating rollcals is here below:

def create_roll(request, id):
    if request.user.is_authenticated and request.user.is_admin or request.user.is_teacher:
        user = get_object_or_404(User, id=id)
        if user.is_student and request.user.part_of == user.part_of or request.user.is_admin:
            if request.method == "POST":

                form = RollCallForm(request.POST)
                if form.is_valid():

                    instance = form.save(commit=False)
                    instance.student = user
                    instance.save()
                    messages.success(request, 'Roll call added succesfully!')
                    return redirect(reverse('rolls-detail', kwargs={"id":id}))

                else:
                    messages.error(request, 'Correct the errors below')
            else:
                form = RollCallForm()

            context = {
                'form': form,
                'student':user,
                }
            return render(request, 'academics/roll_call/create_roll.html', context )
        else:
            raise Http404
    else:
        raise Http404

def rolls_class(request):
    if request.user.is_authenticated and request.user.is_admin:
        klass = Klasses.objects.all()
        template_name = 'academics/roll_call/rolls_class.html'
        context={
        'klass':klass
        }
        return render(request,template_name,context)
    else:
        raise Http404


def rolls_students(request, id):
    if request.user.is_authenticated:
        klass = get_object_or_404(Klasses, id=id)
        klass_teacher = klass.partof.filter(is_teacher=True)[0]
        if request.user.is_admin or request.user == klass_teacher:
            students = klass.partof.filter(is_student=True)
            context = {
                "klass":klass,
                "students":students,
            }
            template_name = "academics/roll_call/rolls_students.html"
            return render(request, template_name, context)

        else:
            raise Http404
    else:
        raise Http404

def rolls_detail(request, id):
    if request.user.is_authenticated:
        student = get_object_or_404(User, id=id)
        total_present_days = student.rollcall.filter(present=True)
        klass = student.part_of
        teacher = klass.partof.filter(is_teacher=True)[0]
        if request.user == teacher or request.user.is_admin or request.user == student:
            rollcalls = student.rollcall.all()
            context = {
            'student':student,
            'rollcalls':rollcalls,
            'total_present_days':total_present_days,
            }
            template_name = 'academics/roll_call/rolls_details.html'
            return render(request, template_name, context)
        else:
            raise Http404
    else:
        raise Http404
