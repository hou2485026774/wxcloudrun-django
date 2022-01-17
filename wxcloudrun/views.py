import json
import logging

from django.http import JsonResponse
from django.shortcuts import render
from wxcloudrun.models import Counters, Users
from django.core.paginator import Paginator
logger = logging.getLogger('log')
#获取数据
def data(request):
    mes = Users.objects.all()
    result = {"message": 'success', "code": '0', "data": [], "count": 0}
    type = []
    for data in mes:
        dic = {}
        dic['id'] = data.id
        dic['name'] = data.sname
        dic['sex'] = data.sex
        dic['city'] = data.city
        dic['school'] = data.school
        type.append(dic)

    result['count'] = len(type)
    # 前台传来的页数
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    print(page_limit)
    paginator = Paginator(type, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    student_info = [x for x in data]
    result['data'] = student_info
    # students.count()总数据量，layui的table模块要接受的格式
    return JsonResponse(result, safe=False)
