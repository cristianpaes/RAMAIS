from app.models import Ramais,Empresas,Setores
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from rest_framework import viewsets
from app.serializers import ramaisSerializer


class ramaisViewSet(viewsets.ModelViewSet):
    queryset = Ramais.objects.all()
    serializer_class = ramaisSerializer


def lista_ramais(request):
    '''
        Realizando a busca e filtrando na tabela
    '''
    busca = request.GET.get('search')
    if busca:
        name_set = Setores.objects.filter(setor__icontains=busca)
        ramal = Ramais.objects.filter(ramal__icontains = busca) | Ramais.objects.filter(nome_resp__icontains = busca) | Ramais.objects.filter(setor_ramais__in=name_set)
    else:
        ramal = Ramais.objects.all()

    paginator = Paginator(ramal, 5)
    page_number = request.GET.get('page')
    pag_obj = paginator.get_page(page_number)
    return render(request, 'ramais.html', {'ramais': pag_obj})

def lista_emails(request):
    '''
       Realizando a busca e filtrando na tabela
    '''
    busca = request.GET.get('search')


    if busca:
        name_set = Setores.objects.filter(setor__icontains=busca)
        #print(name_set.query)
        #print(name_set)
        email = Ramais.objects.filter(nome_resp__icontains = busca) | Ramais.objects.filter(setor_ramais__in=name_set)

    else:
        email = Ramais.objects.all()

    paginator = Paginator(email, 5)
    page_number = request.GET.get('page')
    pag_obj = paginator.get_page(page_number)
    return render(request, 'emails.html', {'emails':pag_obj} )

def lista_empresas(request):
    empresa = Empresas.objects.all()
    dados = {'empresas':empresa}
    return render(request, 'empresas.html', dados)

def login_edicao(request):
    return render(request, 'login.html')

def logout_edicao(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/login')

@login_required(login_url='/login/')
def ed_ramal(request):
    template_name = 'ramal.html'
    dados = {}
    id_ramal = request.GET.get('id')
    id_setor = Ramais.objects.filter(id=id_ramal).values('setor_ramais')
    id_empresa = Ramais.objects.filter(id=id_ramal).values('empresa_ramais')
    # print(id_setor.query)
    if id_ramal:
        ramal = Ramais.objects.get(id=id_ramal)
        setor = Setores.objects.filter(id=id_setor[0]['setor_ramais'])
        empresa= Empresas.objects.filter(id=id_empresa[0]['empresa_ramais'])
        # print(setor.query)
        dados = { 'ramais': ramal, 'setores': setor, 'empresas': empresa}
    else:
        empresa = Empresas.objects.all()
        setor = Setores.objects.all()
        dados = {'empresas': empresa, 'setores': setor}
    return render(request, template_name, dados)

@login_required(login_url='/login/')
def submit_edicao(request):
    if request.POST:
        ramal = request.POST.get('ramal')
        responsavel= request.POST.get('responsavel')
        email=request.POST.get('email')
        setor=request.POST.get('setor')
        empresa=request.POST.get('empresa')
        id_setor = Setores.objects.get(id=setor)
        id_empresa = Empresas.objects.get(id=empresa)
        id_ramal = request.POST.get('id_ramal')
        print(id_ramal)
        if id_ramal:
          Ramais.objects.filter(id=id_ramal).update(ramal=ramal,
                                                      nome_resp=responsavel,
                                                      email=email,
                                                      setor_ramais=id_setor,
                                                      empresa_ramais=id_empresa)
        else:
            Ramais.objects.create(ramal=ramal,
                                  nome_resp=responsavel,
                                  email=email,
                                  setor_ramais=id_setor,
                                  empresa_ramais=id_empresa)
    return redirect('/')

@login_required(login_url='/login/')
def add_setor(request):
    return render(request, 'setor.html')

@login_required(login_url='/login/')
def submit_setor(request):
    if request.POST:
        setor = request.POST.get('setor')
        Setores.objects.create(setor=setor)

    return redirect('/ramais/edicao/')

@login_required(login_url='/login/')
def delete_ramal(request,id_ramal):
    Ramais.objects.filter(id=id_ramal).delete()
    return redirect('/ramais')

@login_required(login_url='/login/')
def delete_email(request,id_ramal):
    Ramais.objects.filter(id=id_ramal).delete()
    return redirect('/emails')

