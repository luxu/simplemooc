from django.conf.urls import url
from django.contrib.auth.views import login, logout
# from simplemooc.accounts.views import register, dashboard
# from pdb import set_trace

from simplemooc.accounts import views

# set_trace()
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', views.register, name='register'),
    url(r'^editar/$', views.editar, name='editar'),
]
