# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 1:47
# @Author  : indiewar(lzl)

from django.urls import path
from . import views

#这是一个字典，不能{}
urlpatterns = [
    path('',views.blog_list,name="blog_list"),
    path('<int:blog_pk>',views.blog_detail,name="blog_detail"),
    path('type/<int:blog_type_pk>',views.blogs_with_type,name="blogs_with_type"),
    # 写文章
    path('create/', views.article_create, name='article_create'),
    # 更新文章
    path('update/<int:id>/', views.article_update, name='article_update'),
    # 删除文章
    path('delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path('article-safe-delete/<int:id>/',views.article_safe_delete, name='article_safe_delete'),
]