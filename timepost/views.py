from django.shortcuts import render
from .models import Timepost
from log.models import UserProfile
from tutorapp.models import Post
from django.shortcuts import render, redirect
from .forms import TimepostForm
from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from tutorapp.views import post_detail_time


def timepost_create(request):
    # TODO: fix template name or get rid of it
    if request.method == "POST":
        form = TimepostForm(request.POST)
        if form.is_valid():
            timepost = form.save(commit=False)
            timepost.tutor_pk = request.POST.get("tutor_pk", None)
            timepost.save()
            print("success creating!")
            # return redirect('/')
            return post_detail_time(request, timepost)
    print("failure")
    return redirect('/')

