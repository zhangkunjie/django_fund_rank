from _ast import Str
from _functools import reduce
from _operator import and_
import json
from operator import or_
import operator

from django.core import serializers
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render

from fund_rank.models import FundRank
from fund_rank.models import Student


# Create your views here.
def index(request):
    return render(request,"index.html")
def fundindex(request):
    return render(request,"fund_index.html")
def getStudentInfo(request):
    id=request.GET['id']
    print("###############"+str(id))
    student=Student.objects.get(id=id)
    studentJSON=student.to_JSON2()
    print("################"+studentJSON)
    return HttpResponse(studentJSON, content_type='application/json')
def getFundRankList(request):
    draw=request.GET.get('draw')
    select_category=request.GET.get("select_category")
    select_categor_array=select_category.split(",")
    print("@@@@@@@@@@@@@"+str(select_categor_array))
    for s in  select_categor_array:
        print(s)   
    orderByColumns=['category','fund_id','fund_name','cal_date','net_asset_value','accumulative','oneday','oneweek','onemonth','threemonth','sixmonth','oneyear','twoyear','threeyear','thisyear','setup','score']
    order_column=int(request.GET.get("order[0][column]"))
    order_dir=request.GET.get("order[0][dir]")
    order_column_name=orderByColumns[order_column]
    if order_dir=='desc':
       order_column_name="-"+orderByColumns[order_column]   
    start=int(request.GET.get('start'))
    length=start+int(request.GET.get('length'))
    minParamsDict={
                  "oneweek":request.GET.get('minWeek'),
                  "onemonth":request.GET.get('minMonth'),
                  "threemonth":request.GET.get('minThreeMonth'),
                  "sixmonth":request.GET.get('minSixMonth'),
                  "oneyear":request.GET.get('minOneYear'),
                  "twoyear":request.GET.get('minTwoYear'),
                  "threeyear":request.GET.get('minThreeYear'),
                  "thisyear":request.GET.get('minThisYear'),
                  "setup":request.GET.get('minSetUp'),
                  "score":request.GET.get('minScore')
                  }
    minParamsList=[]
    print(minParamsDict)
    for (k, v) in  minParamsDict.items():
        q_obj = Q(**{k+"__gte": v})
        minParamsList.append(q_obj)
    fundRankAllListCount=FundRank.objects.all().count()
    fundRankList=FundRank.objects.filter(reduce(operator.and_, minParamsList)).filter(category__in=select_categor_array)
    fundRankPageList=FundRank.objects.filter(reduce(and_, minParamsList)).filter(category__in=select_categor_array).order_by(order_column_name)[start:length]
    fundRankPageListJSON = serializers.serialize('json',fundRankPageList,ensure_ascii=False)
    recordsFiltered=fundRankList.count()
    print("################"+'{"data":'+fundRankPageListJSON+',"recordsTotal":53,"recordsFiltered":33}')
    return HttpResponse('{"data":'+fundRankPageListJSON+',"recordsTotal":'+str(fundRankAllListCount)+',"recordsFiltered":'+str(recordsFiltered)+',"draw":'+draw+'}', content_type='application/json')
