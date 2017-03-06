from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^log$', views.user_log_api, name='user_log_api'),
    url(r'^graph$', views.user_log_graph, name='user_log_graph'),

]