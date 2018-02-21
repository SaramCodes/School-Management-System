from django.shortcuts import render, redirect,get_object_or_404
from .models import User
from .forms import UserCreationForm, UserUpdateForm, LoginForm, SteacherUpdateForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.validators import ValidationError
from django.contrib.auth.forms import PasswordChangeForm



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_creation_view(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == 'POST':
            form = UserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                klass = form.cleaned_data["part_of"]
                user = form.save(commit=False)
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user.set_password(password)
                user.save()
                try:
                    if form.cleaned_data['is_teacher'] == True and klass.partof.filter(is_teacher=True).exists():

                        messages.success(request, 'User Created! BUT')

                        messages.warning(request, "They haven't been added to the class you specified as a teacher is already registered in that class. Open the update page of this user and add them to a new class or make a new class and add them there...")

                        return HttpResponseRedirect(user.get_absolute_url())
                    else:
                        user.part_of = klass
                        user.save()
                        messages.success(request, 'User Created!')
                        return HttpResponseRedirect(user.get_absolute_url())

                except:
                    user.part_of = klass
                    user.save()
                    messages.success(request, 'User Created!')
                    return HttpResponseRedirect(user.get_absolute_url())


        else:
            form = UserCreationForm()
        return render(request, 'accounts/user_creation_view.html', {'form': form})
    else:
        raise Http404


def login_view(request):
    if request.user.is_authenticated():
        raise Http404
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))

                else:
                    messages.error(request, 'Invalid name or password!')
                    return render(request, 'accounts/login_view.html', {'form':form})
        else:
            form = LoginForm()
        return render(request, 'accounts/login_view.html', {'form': form})


def user_view(request):
    if request.user.is_authenticated():
        if request.user.is_admin:
            return render(request, 'accounts/user_view.html', {})
        else:
            raise Http404
    else:
        raise Http404

def user_list(request):
    if request.user.is_authenticated():

        if request.user.is_admin:
            students = User.objects.filter(is_student=True)
            teachers = User.objects.filter(is_teacher=True)
            admins = User.objects.filter(is_admin=True)
            template_name = 'accounts/list-users.html'
            context = {
                'students':students,
                'teachers':teachers,
                'admins':admins,
            }
            return render(request, template_name, context)
        else:
            raise Http404
    else:
        raise Http404


def user_update_view(request, id):
    if request.user.is_authenticated and request.user.is_admin:
        instance = get_object_or_404(User, id=id)
        form = UserUpdateForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            klass = form.cleaned_data["part_of"]
            teacher = form.cleaned_data["is_teacher"]
            if klass:

                if teacher == True and klass.partof.filter(is_teacher=True).exists():
                    messages.error(request, 'A Teacher in that class already exists! Please choose another class.')
                    return render(request, 'accounts/user_update.html', {'form':form})

            instance = form.save(commit=False)

            instance.save()
            messages.success(request, 'User Updated Succesfully!')
            return HttpResponseRedirect(instance.get_absolute_url())


        template_name = "accounts/user_update.html"
        context = {
            "instance": instance,
            "form": form,
        }
        return render(request, template_name, context)
    else:
        raise Http404


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {
            'form': form
        })
    else:
        raise Http404

def user_detail(request, id):
    if not request.user.is_authenticated:
        raise Http404

    user = get_object_or_404(User, id=id)

    user = get_object_or_404(User, id=id)
    template_name = 'accounts/user-detail.html'
    context = {
        "user": user
    }
    return render(request, template_name, context)

    


def user_delete(request, id):
    if not request.user.is_authenticated:
        raise Http404

    if request.user.is_admin:
        instance = get_object_or_404(User, id=id)
        instance.delete()
        messages.success(request, 'Changes saved succesfully!')
        return HttpResponseRedirect(reverse('user-list'))
    else:
        raise Http404

def steacher_update_view(request, id):
    if not request.user.is_authenticated:
        raise Http404

    instance = get_object_or_404(User, id=id)
    if request.user == instance:
        form = SteacherUpdateForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Changes saved succesfully!')
            return HttpResponseRedirect(instance.get_absolute_url())

        template_name = "accounts/steacher_update.html"
        context = {
            "instance": instance,
            "form": form,
        }
        return render(request, template_name, context)
    else:
        raise Http404
