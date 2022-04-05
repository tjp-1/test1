from django.db import models


# 班级主表 模型类
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return u'Clazz:%s' % self.cname


# Create your models here.

# 课程模型类
class Course(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return u'Course:%s' % self.course_name


# 学生模型类
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    cls = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    sname = models.CharField(max_length=30, unique=True)
    cour = models.ManyToManyField(Course)

    def __str__(self):
        return u'Student:%s' % self.sname

    # 重命名数据库表


# 学生证模型表
class Scard(models.Model):
    student = models.OneToOneField(Student, primary_key=True, on_delete=models.CASCADE)
    major = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return u'Scard:%s' % self.major


# 帖子模型类
class Post(models.Model):
    # 编号
    pid = models.AutoField(primary_key=True)  # 自动递增  主键
    # 标题
    title = models.CharField(max_length=100, unique=True)
    # 发帖内容
    content = models.TextField()
    # 创建时间
    create = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)
    # 邮箱
    email = models.EmailField()
    # 判断帖子是否删除
    isdelete = models.BooleanField(default=False)
    # 访问量
    access_count = models.PositiveIntegerField()
    # 价值
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 文件
    file = models.ImageField(upload_to='upload/images/')

    def __str__(self):
        return u'Post:%s,%s' % (self.title, self.access_count)

    class Meta:
        db_table = 't_post'


# 老师模型类
class Teacher(models.Model):
    tno = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=30)
    # 多对多关系
    cour = models.ManyToManyField(Course)

    def __str__(self):
        return u'Trecher:%s' % self.tname


# 获取班级对象
def getCls(cname):
    try:
        cls = Clazz.objects.get(cname=cname)
    except  Exception as ex:
        cls = Clazz.objects.create(cname=cname)
    return cls


# 获取课程对象列表
def getCourseList(*coursenames):
    courseList = []
    for cn in coursenames:
        try:
            c = Course.objects.get(course_name=cn)
        except Exception as ex:
            c = Course.objects.create(course_name=cn)
        courseList.append(c)
    return courseList


def registerStu(sname, cname, *coursenames):
    # 1.插入班级表数据
    cls = getCls(cname)
    # 2.获取课程对象列表
    courseList = getCourseList(*coursenames)
    # 3.插入学生表数据
    try:
        stu = Student.objects.get(sname=sname)
    except Exception as ex:
        stu = Student.objects.create(sname=sname, cls=cls)
        # 4.插入中间表数据
        stu.cour.add(*courseList)
    return True