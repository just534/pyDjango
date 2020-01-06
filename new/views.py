from django.shortcuts import render,HttpResponse
from .models import Score,Student,Course,Teacher
from django.db.models import Avg,Count,Sum,Q


# Create your views here.
def index1(request):
    rows=Student.objects.annotate(avg=Avg('score__number')).filter(avg__gte=60).values('id','avg')
    for row in rows:
        print(row['id'])
    return  HttpResponse("查询成功")


def index2(request):
    rows=Student.objects\
        .annotate(count_num=Count('score__course'),total_score=Sum('score__number'))\
        .values("id", "name", "count_num", "total_score")
    for row in rows:
        print(row)
    return  HttpResponse("查询成功2")