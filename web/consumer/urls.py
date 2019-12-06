from django.conf.urls import include,url
import views

urlpatterns = [
    url(r'^$',views.consumer),
    url(r'add_user$',views.add_user),
    url(r'user_delete$',views.user_delete),
    url(r'user_edit$',views.user_edit),
    url(r'lock_user$',views.user_lock),
    url(r'reset_pwd$',views.reset_pwd)
]
