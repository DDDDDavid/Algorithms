# python 建web server

python 3 版本，执行命令
python -m http.server 8000
python 2 版本，执行命令
python -m SimpleHttpServer 8000

然后在浏览器输入： 
http://localhost:8000

## django 框架
### 教程：http://www.runoob.com/django/django-tutorial.html
1、安装
    pip install django
2、测试
    import django
    django.get_version() 或 django.VERSION
3、创建项目
    django-admin.py startproject testdj
    （也可以用 django-admin startproject HelloWorld）
4、启动服务
    cd testdj
    python manage.py runserver
5、访问
    地址为http://127.0.0.1:8000/

## 释放端口
1、查看系统当前所有被占用端口
    netstat -tln
2、根据端口查询进程,输入
    lsof -i :8000（端口）
3、根据进程杀死任务释放端口
    kill -9 XXXX（进程号）

