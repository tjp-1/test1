from django.shortcuts import render

from .models import *
import math
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# 分页显示数据--原生
# 页码    num     每页显示记录数:size
#  1      2         [0:2]
#  2      2         [2:4]
#  3      2         [4:6]
#  num    size    [(num-1)*size : (num*size)]


# Create your views here.
# 原生处理页码
def page(num, size=18):
    # 接收当前页码数
    num = int(num)

    # 总记录数
    totalRecords = Movie.objects.count()
    # 总页数
    totalPages = int(math.ceil(totalRecords * 1.0 / size))  # 向上取整
    # 判断是否越界
    if num < 1:
        num = 1
    if num > totalPages:
        num = totalPages
    # 计算出每页显示的记录
    movies = Movie.objects.all()[(num - 1) * size:(num * size)]
    return movies, num


# 原生分页
def movie_view(request):
    # 接收前端请求参数  num
    num = request.GET.get('num', 1)

    # 处理分页请求
    movies, n = page(num)
    # 上一页的页码
    pre_page_num = n - 1
    # 下一页的页码
    next_page_num = n + 1

    return render(request,
                  'movie.html',
                  {'movies': movies,
                   'pre_page_num': pre_page_num,
                   'next_page_num': next_page_num
                   })


# django分页
def movie_index_view(request):
    # 获取当前页码数
    num = int(request.GET.get('num', 1))
    # 查询所有数据
    movies = Movie.objects.all()
    # 创建分页器对象
    pager = Paginator(movies, 18)
    # 获取当前页数据
    try:
        perpage_data = pager.page(num)
    except PageNotAnInteger:
        # 如果传入的不是一个整型数据，传入第一页数据
        perpage_data = pager.page(1)
    except EmptyPage:
        # 如果传入的页码不存在，传入最后一页数据
        perpage_data = pager.page(pager.num_pages)

    # 每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    # 每页结束页码
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    return render(request, 'movie.html', {'pager': pager, 'pageList': pageList, "movies": perpage_data, 'num': num})
