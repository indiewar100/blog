# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 12:20
# @Author  : indiewar(lzl)
from django.shortcuts import render_to_response, get_object_or_404, render


def home(request):
    context = {}
    return render(request,'home.html',context)