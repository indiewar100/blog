# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 12:24
# @Author  : indiewar(lzl)
from django import forms
# 引入文章模型
from .models import Blog,BlogType

# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Blog
        # 定义表单包含的字段
        fields = ('title', 'content','blog_type')