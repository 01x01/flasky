# coding: utf-8

from app import create_app,db
from app.models import User,Role

app = create_app("default")


# flask shell要载入的变量
@app.shell_context_processor
def make_shell_context():
    return {'db': db,"User":User,"Role":Role}