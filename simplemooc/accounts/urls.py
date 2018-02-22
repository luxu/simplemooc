from django.conf.urls import url
from django.contrib.auth.views import login, logout
from simplemooc.accounts.views import dashboard
from simplemooc.accounts.views import register
from simplemooc.accounts.views import password_reset
from simplemooc.accounts.views import password_reset_confirm
from simplemooc.accounts.views import edit
from simplemooc.accounts.views import edit_password
# from pdb import set_trace


# set_trace()
urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^entrar/$', login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', register, name='register'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),
]
