from django.conf.urls import include,url
import views

urlpatterns = [
    url(r'^$',views.deploy),
    url(r'deploy_edit$',views.deploy_edit),
    url(r'deploy_delete$',views.deploy_del),
]
