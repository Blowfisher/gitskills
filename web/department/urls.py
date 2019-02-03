from django.conf.urls import include,url
import views

urlpatterns = [
    url(r'^$',views.department),
    url(r'^department_delete$',views.dpt_del),
    url(r'^department_add',views.dpt_add),
    url(r'^department_lock',views.dpt_lock),
    url(r'^department_edit',views.dpt_edit),
    url(r'^department_user',views.dpt_user),
]
