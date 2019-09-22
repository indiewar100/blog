# blog

> 基于python Django 实现的简易blog


This repository contains:

1. 文章的增删查改
2. 简单的权限管理
3. 用bootstrap实现的普通前端展示

## Background

数据库小作业，只实现了简单的增删查改功能。

## Usage

### 运行
修改myblog/setting.py 修改数据库配置

### 创建数据库
创建数据库后，终端下执行:
```python
./manage.py makemigrations
./manage.py migrate
```
### 创建超级用户
```python
./manage.py createsuperuser
```
### 开始运行：
```python
./manage.py runserver
```
浏览器打开: http://127.0.0.1:8000/ 

## License

[MIT](LICENSE) © indiewar100