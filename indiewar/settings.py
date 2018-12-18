import os

#获取当前文件所在的绝对路径
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY','secret string')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Indiewar Admin', MAIL_USERNAME)

    INDIEWAR_EMAIL = os.getenv('INDIEWAR_EMAIL')
    INDIEWAR_POST_PER_PAGE = 10
    INDIEWAR_MANAGE_POST_PER_PAGE = 15
    INDIEWAR_COMMENT_PER_PAGE = 15



class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL' ,
                              'sqlite:///' + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Production': ProductionConfig,
    'default': DevelopmentConfig
}
