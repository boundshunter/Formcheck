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


def fm(request):
    if request.method == 'GET':
        obj = FM()
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