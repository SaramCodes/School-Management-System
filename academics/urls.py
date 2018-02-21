from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    #subject views
    subject_create_view,
    subject_list_view,
    subject_detail_view,
    subject_delete_view,
    subject_update_view,
    #subject views <--end-->
    #grade views
    semester_view,
    semester_create_view,
    grade_klass_list_view,
    grade_student_list_view,
    grade_create_view,
    grade_detail_view,
    #for teachers
    grade_view_for_teacher,
    grade_detail_view_teacher,
    grade_create_view_teacher
    )



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="academics/academics_view.html"), name='academics_view'),
    #SUBJECTS
    url(r'^subjects/create$', subject_create_view, name='subject-create'),
    url(r'^subjects$', subject_list_view, name='subject-list'),
    url(r'^(?P<id>[\w-]+)/$', subject_detail_view, name='subject-detail'),
    url(r'^(?P<id>[\w-]+)/delete$', subject_delete_view, name='subject-delete'),
    url(r'^(?P<id>[\w-]+)/update$', subject_update_view, name='subject-update'),
    # SUBJECTS <--END-->

    # GRADES
    # I am beginning the grades view by listing the semesters first.
    #So the first url will be of semester model.
    url(r'^grades/semester/$', semester_view, name='semester-view'),
    url(r'^semester/create$', semester_create_view, name='semester-create'),
    url(r'^grades/semester/(?P<id>[\w-]+)/$', grade_klass_list_view, name='grade-klass-list'),

    url(r'^grades/(?P<semester_id>(\d+))/semester/(?P<klass_id>(\d+))$', grade_student_list_view, name='grade-klass-student-list'),

    #above view but for teachers
    url(r'^grade/(?P<semester_id>(\d+))/semester/(?P<klass_id>(\d+))$', grade_view_for_teacher, name='grade-view-for-teacher'),

    url(r'^grades/(?P<semester_id>(\d+))/student/(?P<student_id>(\d+))$', grade_detail_view, name='grade-detail'),

    url(r'^grade/(?P<semester_id>(\d+))/student/(?P<student_id>(\d+))$', grade_detail_view_teacher, name='grade-detail-teacher'),

    url(r'^grades/(?P<semester_id>(\d+))/student/(?P<student_id>(\d+))/create/$', grade_create_view, name='grade-create'),

    url(r'^grade/(?P<semester_id>(\d+))/student/(?P<student_id>(\d+))/create/$', grade_create_view_teacher, name='grade-create-teacher'),


]
