from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from django import forms
# Create your views here.


# Form 验证
from django.forms import widgets
from django.forms import fields


class FM(forms.Form):
    user = fields.CharField(error_messages={'required':'用户名不能为空'},
                            widget=widgets.Input(attrs={'class': 'c1'}),
                            label="用户名"
                            )

    pwd = fields.CharField(max_length=12, min_length=6, error_messages={'required':'密码不能为空', 'max_length': '密码长度不能大于12位', 'min_length': '密码长度不能小于6位'},
                           widget=widgets.PasswordInput(attrs={'class': 'c2'}),
                           label="密码"
                           )

    email = fields.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
                              label="邮箱"
                              )
    f = fields.FileField(allow_empty_file=False)

    p = fields.FilePathField(path='app01') # 列出app01目录下所有文件

    city1 = fields.ChoiceField(
        choices=[(0, '北京'), (1, '吉林'), (2, '银川')]
    )
    city2 = fields.MultipleChoiceField(
        choices=[(0, '广东'), (1, '深圳'), (2, '东莞')]
    )


def fm(request):
    if request.method == 'GET':
        dic = {
            'user': 'a1',
            'pwd': 'abc',
            'email': 'aa@test.com',
            'city1': 2,
            'city2': [0, 1],
        }
        obj = FM(initial=dic) # 设置初始值，必须是个字典，字典中值的获取可以是从数据库中获得可以手动指定
        return render(request, 'fm.html', {'obj': obj})
    elif request.method == 'POST':
        # 获取用户所有数据
        # 没调数据请求的验证
        # 成功：获取所有的正确信息
        # 失败：显示错误信息
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1: # not null   True
            print(obj.cleaned_data)
        else:
            print(obj.errors)
            return render(request, 'fm.html', {'ojb': obj})
        return redirect('/fm/')