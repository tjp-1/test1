from django.contrib import admin

# Register your models here.

from .models import *

# 注册模型类
admin.site.register(Student)
# 注册邮箱类
admin.site.register(Post)
# 注册学生证类
admin.site.register(Scard)
# 注册班级类
admin.site.register(Clazz)
# 注册老师类
admin.site.register(Teacher)
# 注册课程类
admin.site.register(Course)
