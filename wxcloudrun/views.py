import json
import logging

from django.http import JsonResponse, HttpResponse
from wxcloudrun.models import Users
from django.core.paginator import Paginator
logger = logging.getLogger('log')
#登录
def login(request):
    result = {"msg": '', "code": '0'}
    sname = request.POST.get('sname')
    spwd = request.POST.get('spwd')
    print(sname,'',spwd)
    u = Users.objects.get(sname=sname)
    if u.spwd ==spwd:
        result['msg'] = '登录成功'
    else:
        result['msg'] = 'flase'
    return JsonResponse(result)
#获取用户数据
def data(request):
    mes = Users.objects.all()
    result = {"message": 'success', "code": '0', "data": [], "count": 0}
    type = []
    for data in mes:
        dic = {}
        dic['id'] = data.id
        dic['sname'] = data.sname
        dic['sex'] = data.sex
        dic['city'] = data.city
        dic['school'] = data.school
        type.append(dic)

    result['count'] = len(type)
    # 前台传来的页数
    page_index = request.GET.get('page','1')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit','5')
    # 分页器进行分配
    print(page_limit)
    paginator = Paginator(type, page_limit)#将数据进行根据limit数量进行分割
    # 前端传来页数的数据 再根据页数将数据传回去
    data = paginator.page(page_index)
    print("123",data)
    # 放在一个列表里
    student_info = [x for x in data]
    result['data'] = student_info
    print(student_info)
    # students.count()总数据量，layui的table模块要接受的格式
    return JsonResponse(result, safe=False)
def doadd(request):
    if request.method == 'POST':
        response = {'msg': '', 'status': False}
        sname = request.POST.get('sname', '')
        city = request.POST.get('city', '')
        sex = request.POST.get('sex', '')
        school = request.POST.get('school', '')
        spwd = request.POST.get('spwd', '')
        print(sname+"+++++++"+city+''+school)
        u= Users.objects.create(sname=sname,city=city,sex=sex,school=school,spwd=spwd)
        u.save()
        response['msg'] = '添加成功'
        response['status'] = True
        return HttpResponse(json.dumps(response))
#将前端传回的数据进行更新
def doedit(request):
    # result = {"msg": 'success', "code": '0', "data": [], "count": 0}
    if request.method == 'POST':
        response = {'msg': '', 'status': False}
        sname = request.POST.get('sname', '')
        city = request.POST.get('city', '')
        id = request.POST.get('id', '')
        sex = request.POST.get('sex', '')
        school = request.POST.get('school', '')
        print("需要修改的"+sname+"+++++++"+city+''+id)
        u= Users.objects.filter(id=id)
        u.update(sname=sname,city=city,sex=sex,school=school)
        response['msg'] = '更新成功'
        response['status'] = True
        return HttpResponse(json.dumps(response))
def delete(request):
    if request.method == 'POST':
        response = {'msg': '', 'status': False}
        id = request.POST.get('id', '')
        print("要删除的id"+id)
        Users.objects.filter(id=id).delete()
        response['msg'] = '删除成功'
        response['status'] = True
        return HttpResponse(json.dumps(response))
# def uploadImg(request):
#     response = {'msg': '', 'status': False}
#     if request.method == 'POST':
#         img = request.FILES.get('img')
#         print("要上传的图片",img)
#         i= Img.objects.create(img=img)
#         i.save()
#         response['msg'] = '666'
#     return JsonResponse(response,safe=False)
#得到图片数据
# def getImg(request):
#     if request.method == 'POST':
#         result = {"msg": '666', "code": '0','data':[]}
#         mes = Img.objects.all()
#         print(mes)
#         line = []
#         for data in mes:
#             dic = {}
#             dic['id'] = data.id
#             dic['img'] = str(data.img)
#             line.append(dic)
#             print(line)
#         result['data'] = line
#         return JsonResponse(result, safe=False)