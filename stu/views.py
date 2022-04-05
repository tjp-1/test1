from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index_view(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 1.获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        # 2.查询数据库
        if uname and pwd:
            # 查询数据库数据
            c = Student.objects.filter(sname=uname, spwd=pwd).count()
            if c == 1:
                return HttpResponse('登录成功')
        # 3.判断是否登录成功
        return HttpResponse('登录失败')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        if uname and pwd:
            # 创建模型对象
            stu = Student(sname=uname, spwd=pwd)
            # 插入数据库
            stu.save()
            return HttpResponse('注册成功!')
        return HttpResponse('注册失败!')


def show_view(request):
    # 1.查询数据库中的数据  stu_student表中的数据
    stus = Student.objects.all()
    return render(request, 'show.html', {'students': stus})


def info_view(request):
    if request.method == 'GET':
        return render(request, 'info.html')
    else:
        # 接收请求参数
        sname = request.POST.get('sname', '')
        cname = request.POST.get('clsname', '')
        coursenames = request.POST.getlist('coursname', [])
        print(coursenames)
        # 将数据注册到数据库
        flag = registerStu(sname, cname, *coursenames)
        if flag:
            return HttpResponse('注册成功！')
        return HttpResponse('注册失败！')


# 显示所有的班级信息
def showInfo_view(request):
    # 查询班级表中的所有数据
    clszzList = Clazz.objects.all()
    return render(request, 'infoShow.html', {'cls': clszzList})


# 显示当前班级下的所有学生信息
def getStu_view(request):
    # 获取请求信息
    cno = request.GET.get('cno', '')
    cno = int(cno)
    # 根据班级编号获取所有学生
    stus = Clazz.objects.get(cno=cno).student_set.all()
    # for s in stus:
    #     print(s.sname,s.cls.cname)
    #     for cou in s.cour.all():
    #         print(cou.course_name)
    return render(request, 'stuShow.html', {'stus': stus})
