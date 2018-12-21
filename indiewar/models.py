from indiewar.extensions import db
from datetime import datetime

#管理员
class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(60))
    name = db.Column(db.String(50))
    about = db.Column(db.Text)

#分类
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)#名称不能相同
    posts = db.relationship('Post', back_populates='category')#分类与文章有一对多的关系

#文章
class  Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)

    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',back_populates='posts')

#评论
class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(260))
    site = db.Column(db.String(260))
    body = db.Column(db.Text)
    from_admin = db.Column(db.Boolean, default=False)#是否为管理员评论，默认false
    reviewed = db.Column(db.Boolean, default=False)#默认不通过审核
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    #添加一个外键指向它本身，得到一种层级关系
    replied_id = db.Column(db.Integer,db.ForeignKey('comment.id'))
    replied = db.relationship('Comment',back_populates = 'replies')
    repplies = db.relationship('Comment',back_populates = 'comment.id')
