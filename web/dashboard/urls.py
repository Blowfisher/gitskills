from django.conf.urls import include,url
import views
from views import *

urlpatterns = [
    url(r'^$/',views.dashboard),
    url(r'^guider/$',views.guider),
]
