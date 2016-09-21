from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from . import views
from .views import (
    CreateReport,
    ListReport,
    ListMyReport,
    DetailReport,
    UpdateReport,
    DeleteReport,
    CreateUser,
    CreateScore,
    UpdateScore
)

urlpatterns = [
    url(r'^report_entries/', login_required(CreateReport.as_view()), name='create_report'),
    url(r'^search/', login_required(views.search), name='search'),
    url(r'^index/', login_required(ListReport.as_view()), name='index'),
    url(r'^mypage/', login_required(ListMyReport.as_view()), name='mypage'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(DetailReport.as_view()), name='detail_report'),
    url(r'^(?P<pk>[0-9]+)/edition/$', login_required(UpdateReport.as_view()), name='update_report'),
    url(r'^(?P<pk>[0-9]+)/delete/$', login_required(DeleteReport.as_view()), name='delete_report'),
    url(r'^login/', login, {'template_name': 'report/login.html'}, name='login'),
    url(r'^user_register/$', CreateUser.as_view(), name='create_user'),
    url(r'^logout/$', logout, {'template_name': 'report/logout.html'}, name='logout'),
    url(r'^(\w+)/score/', login_required(CreateScore.as_view()), name='create_score'),
    url(r'^(?P<pk>[0-9]+)/edition/$', login_required(UpdateScore.as_view()), name='update_score'),
]
