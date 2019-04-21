from . import main
from .views import Index


# 第一个参数是 http://127.0.0.1:5000/index/xxx 的 /xxx， 这里是 /
# 第二个参数给这个视图函数命名，方便后面的查找，如 url_for('main.index') 即可查找到这个功能函数
main.add_url_rule('/',view_func=Index.as_view('index'))