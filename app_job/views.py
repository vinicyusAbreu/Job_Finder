from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Emprego
from django.db.models import Q

# Create your views here.


def PostJob(request):
    emp = Emprego.objects.all().order_by('-id').values()
    nv = emp[:2]
    for vaga_nova in nv:
        for em in emp:
            if vaga_nova['id']==em['id']:
                em['vaga']='new-job'
                
                
    paginator = Paginator(emp, 4)
    page = request.GET.get('page')
    emp = paginator.get_page(page)
    

                
    return render(request, 'app_job/index.html', {"jobs": emp})


def Formulario(request):
    return render(request, 'app_job/formulario.html')


def Detalhes(request, vaga_id):
    vaga = Emprego.objects.filter(id=vaga_id)
    return render(request, 'app_job/detalhe.html', {"vagas": vaga})


def NovaVaga(request):
    if request.method == 'POST':
        titulo = request.POST.get('title')
        descricao = request.POST.get('description')
        empresa = request.POST.get('company')
        email = request.POST.get('email')
        salario_vaga = request.POST.get('salary')
        if request.FILES.get('foto'):
            imagem = request.FILES['foto']

        else:
            imagem = None

        if titulo.strip() == '' or descricao.strip() == '' or empresa.strip() == '' or descricao.strip() == '' or email.strip() == '' or salario_vaga.strip() == '':
            messages.add_message(request, messages.ERROR,
                                 'Nenhum campo pode ficar vazio.')
            return render(request, 'app_job/formulario.html')

    vaga = Emprego.objects.create(
        titulo_vaga=titulo, descricao_vaga=descricao, empresa_contratante=empresa, email_contato=email, salario=salario_vaga, imagem_empresa=imagem)

    vaga.save()
    return redirect('index')


def Busca(request):
    buscar = request.GET.get('job')
    if buscar.strip() == '':
        return redirect('index')
    
    qs = Q(titulo_vaga__icontains=buscar)
    
    emp = Emprego.objects.filter(qs)
    
    paginator = Paginator(emp, 4)
    
    page = request.GET.get('page')
    
    emp = paginator.get_page(page)
    
    return render(request, 'app_job/busca.html', {"jobs": emp})
