# coding:utf-8
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # 邮件设置
    MAIL_SERVER=os.getenv('MAIL_SERVER')
    MAIL_USE_LTS=os.getenv('MAIL_USE_LTS')
    MAIL_USERNAME=os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX='[Flask]'
    MAIL_SENDER=os.getenv('MAIL_USERNAME')
    MAIL_PORT=os.getenv("MAIL_PORT")
    FLASK_MAIL_SUBJEJCT_PREFIX=os.getenv("FLASK_MAIL_SUBJEJCT_PREFIX")

    # 数据库设置
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI')

    # Admin
    ADMIN=os.getenv("ADMIN")


    # 拓展方法，在载入配置时，可先行执行进行配置
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProdConfig(Config):
    pass


#
config = {
    "default": Config,
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProdConfig
}