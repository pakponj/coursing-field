from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def browseIndex(req):
    '''Return the last courses.'''
    example_list = [
    {
        'courseName': 'Machine Learning',
        'courseThumnail': 'http://i.imgur.com/TGApdwy.jpg',
        'courseOwner': 'Andrew Ng',
        'courseRating': 4.5
    },
    {
        'courseName': 'Hidan no Aria',
        'courseThumnail': 'https://upic.me/i/6p/9untitled.png',
        'courseOwner': 'J.C. Staff',
        'courseRating': 3
    },
    {
        'courseName': 'Kinzu',
        'courseThumnail': 'https://upic.me/i/kr/kinzu.png',
        'courseOwner': 'SteelSeries',
        'courseRating': 3.5
    },
    {
        'courseName': 'Mac',
        'courseThumnail': 'https://upic.me/i/ow/0picture1.png',
        'courseOwner': 'Steve Jobs',
        'courseRating': 1
    },
    {
        'courseName': 'HDD',
        'courseThumnail': 'https://upic.me/i/dq/60untitled.jpg',
        'courseOwner': 'Western Digital',
        'courseRating': 2.5
    },
    {
        'courseName': 'PSU',
        'courseThumnail': 'https://upic.me/i/zq/image0398.jpg',
        'courseOwner': 'Corsair',
        'courseRating': 1
    },
    {
        'courseName': 'WD 1TB',
        'courseThumnail': 'https://upic.me/i/3z/image0397.jpg',
        'courseOwner': 'Sandisk',
        'courseRating': 5
    },
    {
        'courseName': 'Aegisub on Mac',
        'courseThumnail': 'https://upic.me/i/9e/1picture1.png',
        'courseOwner': 'Aegisub',
        'courseRating': 4.3
    },
    {
        'courseName': 'Miku on Mac',
        'courseThumnail': 'https://upic.me/i/rs/picture1.png',
        'courseOwner': 'Krypton Future Media Works',
        'courseRating': 3.7
    },
    {
        'courseName': 'Copying speed',
        'courseThumnail': 'https://upic.me/i/2o/10untitled.png',
        'courseOwner': 'Microsoft',
        'courseRating': 3
    },
    {
        'courseName': 'Hideyoshi',
        'courseThumnail': 'https://upic.me/i/0p/snapshot20110419211211.jpg',
        'courseOwner': 'BakaTest',
        'courseRating': 9999
    },
    {
        'courseName': 'Installing mac os',
        'courseThumnail': 'https://upic.me/i/vw/11untitled.png',
        'courseOwner': 'VMware',
        'courseRating': 0
    },
    {
        'courseName': 'Mac desktop',
        'courseThumnail': 'https://upic.me/i/w3/0picture1.png',
        'courseOwner': 'Hackintoch',
        'courseRating': 3
    },
    {
        'courseName': 'Daiteikoku',
        'courseOwner': 'Alicesoft',
        'courseThumnail': 'https://upic.me/i/jh/62untitled.jpg',
        'courseRating': 3
    }]
    paginator = Paginator(example_list, 4)
    page = req.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(req ,'browse/index.html', {'pageTitle': 'Browse courses', 'browseFilter': 'All courses','courses': courses, 'pageRange': paginator.page_range})

def createCourse(req):
    return render(req, 'browse/createCourse.html')
