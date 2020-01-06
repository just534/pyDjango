from django.shortcuts import render,HttpResponse
from .models import Score,Student,Course,Teacher
from django.db.models import Avg,Count,Sum,Q


# Create your views here.
def index1(request):
    rows=Student.objects.annotate(avg=Avg('score__number')).filter(avg__gte=60).values('id','avg')
    for row in rows:
        print(row['id'])
    return  HttpResponse("查询成功")

#
def index2(request):
    rows=Student.objects\
        .annotate(count_num=Count('score__course'),total_score=Sum('score__number'))\
        .values("id", "name", "count_num", "total_score")
    for row in rows:
        print(row)
    return  HttpResponse("查询成功2")

#查询姓“李”的老师的个数；
def index3(request):
    teachercount=Teacher.objects.filter(name__startswith='李').count()
    print(teachercount)
    return  HttpResponse("查询成功3")

def index4(request):
    students=Student.objects.filter(score__course__id__in=[1,2]).values('id','name')
    print(students)
    return  HttpResponse("查询成功4")

def index5(request):
    students=Student.objects.filter(score__course__teacher__name='黄老师')
    for student in students:
        print(student.name)

    return  HttpResponse("查询成功5")


def index6(request):
    students=Student.objects.annotate(num=Count('score__course',filter=Q(score__course__teacher__name='黄老师')))\
        .filter(num=Course.objects.filter(teacher__name='黄老师').count()).values('id','name')
    for student in students:
        print(student)

    return  HttpResponse("查询成功6")


def index7(request):
    students=Student.objects.filter(score__number__lt=60).values('id','name')
    for student in students:
        print(student)

    return  HttpResponse("查询成功7")
def index8(request):
    students=Student.objects.annotate(num=Count('score__course')).filter(num__lt=Course.objects.count())
    for student in students:
        print(student.name)

    return  HttpResponse("查询成功8")