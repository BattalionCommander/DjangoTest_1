from django.shortcuts import render
from .models import User

def index(request):
    # 判断是否是post请求
    if request.method == 'POST':
        # 获取到请求参数， username的写法，如果username不存在不会抛异常
        # password 会抛异常
        username = request.POST.get('username')
        password = request.POST['password']
        u = User(username=username, password=password)
        u.save()

        # 业务 需求：查询出所有数据
        users = User.objects.all()

        # 返回给用户  模版中使用到的users就是这里传递进去的
        return render(request, template_name='index.html', context={
            'users': users
        })

    return render(request, 'index.html')