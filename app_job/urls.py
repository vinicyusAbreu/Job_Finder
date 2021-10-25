from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostJob, name='index'),
    path('formulario/',views.Formulario, name="formulario"),
    path('detalhe/<int:vaga_id>',views.Detalhes, name="detalhes"),
    path('novoEmprego/',views.NovaVaga, name="novoEmprego"),
    path('busca/',views.Busca, name="busca"),
]
