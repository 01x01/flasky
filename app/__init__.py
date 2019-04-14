from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    # 载入配置
    app.config.from_object(config[config_name])
    # 执行配置前需要执行的函数
    config[config_name].init_app(app)

    # 初始化插件
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)

    # 蓝图
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    from .error import error as error_bp
    app.register_blueprint(error_bp)

    return app