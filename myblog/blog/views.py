from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect

from blog.forms import ArticlePostForm
from .models import Blog,BlogType
import markdown

# Create your views here.
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog,pk=blog_pk)
    blog.content = markdown.markdown(blog.content,
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ])
    context['blog'] = blog
    return render(request,'blog/blog_detail.html', context)

def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk = blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog/blogs_with_type.html', context)


def article_create(request):
    if request.method == "POST":
        # 表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 是否满足模型的要求
        if article_post_form.is_valid():
            # 暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            new_article.author = request.user
            # 保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("blog_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {}
        context['article_post_form'] = article_post_form
        context['blog_types'] = BlogType.objects.all()
        # 返回模板
        return render(request, 'blog/create.html', context)

def article_update(request, id):
    """
    更新文章的视图函数
    GET方法进入初始表单页面
    id： 文章的 id
    """

    # 获取需要修改的具体文章对象
    article = Blog.objects.get(id=id)
    if request.user == article.author or request.user.is_superuser :
        # 判断用户是否为 POST 提交表单数据
        if request.method == "POST":
            # 将提交的数据赋值到表单实例中
            article_post_form = ArticlePostForm(data=request.POST)
            # 判断提交的数据是否满足模型的要求
            if article_post_form.is_valid():
                # 保存新写入的 title、body 数据并保存
                article.title = request.POST['title']
                article.content = request.POST['content']

                blog_type_id = request.POST['blog_type']
                article.blog_type = BlogType.objects.get(id=blog_type_id)


                article.save()
                return redirect("blog_detail",id)
            # 如果数据不合法，返回错误信息
            else:
                return HttpResponse("表单内容有误，请重新填写。")

        # 如果用户 GET 请求获取数据
        else:
            article_post_form = ArticlePostForm()
            # 提取旧的内容
            context = {}
            context['article'] = article
            context['article_post_form'] = article_post_form
            context['blog_types'] = BlogType.objects.all()

            # 将响应返回到模板中
            return render(request, 'blog/update.html', context)
    else:
        return HttpResponse("无权限。")


# 删文章
def article_delete(request, id):
    article = Blog.objects.get(id=id)
    if request.user == article.author or request.user.is_superuser :
        # 调用.delete()方法删除文章
        article.delete()
        # 完成删除后返回文章列表
        return redirect("blog_list")
    else:
        return HttpResponse("无权限。")


# 安全删除文章
def article_safe_delete(request, id):
    article = Blog.objects.get(id=id)
    if request.user == article.author or request.user.is_superuser:
        if request.method == 'POST':
            article.delete()
            return redirect("blog_list")
        else:
            return HttpResponse("仅允许post请求")
    else:
        return HttpResponse("无权限。")