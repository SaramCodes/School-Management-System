from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from accounts.models import User
from .models import Klasses
from .forms import KlassesForm,KlassesUpdateForm



#Everything related to KLASSES is here

def klasses_list_view(request):
    if request.user.is_authenticated and request.user.is_admin:
        klasses = Klasses.objects.all()
        template_name = "klass/klasses_list_view.html"
        context = {"klasses":klasses}

        return render(request, template_name, context)
    else:
        raise Http404


def klasses_detail_view(request, id):
    if request.user.is_authenticated:
        klass = get_object_or_404(Klasses, id=id)
        if request.user.is_admin or request.user in klass.partof.filter(is_teacher=True) or request.user in klass.partof.filter(is_student=True):
            total_num = klass.partof.filter(is_student=True).count()


            teacher = klass.partof.filter(is_teacher=True)
            students = klass.partof.filter(is_student=True)
            template_name = "klass/klasses_detail_view.html"
            context = {
            "klass":klass,
            "teacher":teacher,
            "students":students,
            "total_num":total_num,
            }
            return render(request, template_name, context)
        else:
            raise Http404

    else:
        raise Http404


def klasses_create_view(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == 'POST':
            form = KlassesForm(request.POST)
            if form.is_valid():
                try:
                    students = form.cleaned_data.get("students")
                    teacher = form.cleaned_data.get("teacher")
                    klass = form.save(commit=False)
                    klass.save()
                    teacher.part_of = klass
                    teacher.save()
                    for student in students:
                        student.part_of = klass
                        student.save()
                    messages.success(request, 'Class Created SucessFully!!')
                    return HttpResponseRedirect(klass.get_absolute_url())
                except:
                    students = form.cleaned_data.get("students")
                    klass = form.save(commit=False)
                    klass.save()
                    if students:
                        for student in students:
                            student.part_of = klass
                            student.save()

                    messages.success(request, 'Class Created SucessFully!!')
                    return HttpResponseRedirect(klass.get_absolute_url())

        else:
            form = KlassesForm()
        return render(request, 'klass/klasses_create_view.html', {'form': form})
    else:
        raise Http404



def klasses_update_view(request, id):
    instance = get_object_or_404(Klasses, id=id)
    form = KlassesUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Class Updated SucessFully!!')
        return HttpResponseRedirect(instance.get_absolute_url())

    else:
        return render(request, "klass/klasses_update_view.html", context = {
            "instance": instance,
            "form": form,
        })




def klasses_delete_view(request, id):
    if request.user.is_authenticated and request.user.is_admin:
        instance = get_object_or_404(Klasses, id=id)
        instance.delete()
        messages.success(request, 'Klass Deleted Succesfully')
        return HttpResponseRedirect(reverse('klasses_list_view'))
    else:
        raise Http404
