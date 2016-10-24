from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=50)
    courseDesc = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    courseThumbnail = models.ImageField(upload_to='thumbnails/')
    coursePrice = models.IntegerField()
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    isDelete = models.BooleanField()

class Video(models.Model):
    videoID = models.AutoField(primary_key=True)
    videoName = models.CharField(max_length=50)
    videoFile = models.FileField(upload_to='videos/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now=False,auto_now_add=True)
    isDelete = models.BooleanField()

class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    commentDesc = models.CharField(max_length=250)
    commentDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    isDelete = models.BooleanField()

class Transaction(models.Model):
    transactionID = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    transactionDate = models.DateTimeField(auto_now=False, auto_now_add=True)

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=50)

class CourseInCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    reviewDesc = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    reviewDate = models.DateTimeField(auto_now=False,auto_now_add=True)
    isDelete = models.BooleanField()

class Coupon(models.Model):
    couponSerial = models.IntegerField(primary_key=True)
    couponDesc = models.CharField(max_length=250)
    value = models.IntegerField()
    percent = models.IntegerField()
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    isUsed = models.BooleanField()

class TakenCourse(models.Model):
    takenCourseID = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    taker = models.ForeignKey(User, on_delete=models.CASCADE)
