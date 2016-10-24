from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# Create your views here.
def createCourse(req):
    return render(req, 'course/createCourse.html')

def createNewCourse(req):
    return redirect(reverse('course:createCourse'))
