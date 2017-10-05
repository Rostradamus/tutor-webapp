from django.shortcuts import render
from .models import Timepost
from log.models import UserProfile
from tutorapp.models import Post
from django.shortcuts import render, redirect
from .forms import TimepostForm
from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect


def timepost_create_helper(form, post_pk):
        student_username = form.get("student_username", None)
        tutor_pk = form.get("tutor_pk", None)
        course_name = form.get("course_name", None)
        course_number = form.get("course_number", None)
        days = form.get("days", None)
        start_time = form.get("start_time", None)
        end_time = form.get("end_time", None)

        timepost = TimepostForm(form or None)
        timepost['student_username'] = student_username
        timepost['tutor_pk'] = tutor_pk
        timepost['course_name'] = course_name
        timepost['course_number'] = course_number
        timepost['days'] = days
        timepost['start_time'] = start_time
        timepost['end_time'] = end_time
        timepost.save()


def timepost_create(request, pk):
        #TODO: fix template name or get rid of it
        template_name = 'post_add_time.html'
        formset_obj = formset_factory(TimepostForm)
        if request.method == 'GET':
                formset = formset_obj(request.GET or None)
                return render(request, template_name, {'formset': formset})
        elif request.method == 'POST':
                formset = formset_obj(request.POST or None)
                if formset.is_valid():
                    for form in formset:
                        timepost_create_helper(form, pk)
                        # do necessary action here
                        # redirect from here or return success message
                # in case the form is not valid, return as it is
                        return redirect('post_detail', pk = pk)
        return redirect("/")

