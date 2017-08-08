from _ast import Str
import json

from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render

from fund_rank.models import FundRank
from fund_rank.models import Student


# Create your views here.
def index(request):
    return render(request,"index.html")
def getStudentInfo(request):
    id=request.GET['id']
    print("###############"+str(id))
    student=Student.objects.get(id=id)
    studentJSON=student.to_JSON2()
    print("################"+studentJSON)
    return HttpResponse(studentJSON, content_type='application/json')
def getFundRankList(request):
    fundRankList=FundRank.objects.all()
    fundRankListJSON = serializers.serialize('json',fundRankList,ensure_ascii=False)
    print("################"+'{"data":'+fundRankListJSON+"}")
    return HttpResponse(fundRankListJSON, content_type='application/json')
