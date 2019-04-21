from .views import Register,Login,Confirm,Unconfirm,ResendConfirm,Logout
from . import auth
auth.add_url_rule("/login",view_func=Login.as_view('login'))
auth.add_url_rule("/register",view_func=Register.as_view('register'))
auth.add_url_rule("/confirm/<token>",view_func=Confirm.as_view('confirm'))
auth.add_url_rule("/unconfirm",view_func=Unconfirm.as_view('unconfirm'))
auth.add_url_rule("/resend_confirm",view_func=ResendConfirm.as_view('resend_confirm'))
auth.add_url_rule("/logout",view_func=Logout.as_view('logout'))