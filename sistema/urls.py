# url - view - template

from django.urls import path, reverse_lazy
from .views import Manutencoes, Criarconta, Paginaperfil
from django.contrib.auth import views as auth_view

app_name = 'sistema'

urlpatterns = [

    path('manutencoes/', Manutencoes.as_view(), name='manutencoes'),
    path('', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('sistema:manutencoes')), name='mudarsenha'),

]
