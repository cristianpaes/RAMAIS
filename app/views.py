from app.models import Ramais,Empresas,Setores
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def lista_ramais(request):
    '''
        Realizando a busca e filtrando na tabela
    '''
    busca = request.GET.get('search')
    if busca:
        ramal = Ramais.objects.filter(ramal__icontains = busca) | Ramais.objects.filter(nome_resp__icontains = busca)
    else:
        ramal = Ramais.objects.all()

    paginator = Paginator(ramal, 10)
    page_number = request.GET.get('page')
    pag_obj = paginator.get_page(page_number)
    return render(request, 'ramais.html', {'ramais': pag_obj})

def lista_emails(request):
    '''
       Realizando a busca e filtrando na tabela
    '''
    busca = request.GET.get('search')
    if busca:
        email = Ramais.objects.filter(nome_resp__icontains = busca)
    else:
        email = Ramais.objects.all()

    paginator = Paginator(email, 10)
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
    empresa = Empresas.objects.all()
    setor = Setores.objects.all()
    dados = {'empresas': empresa,'setores':setor}
    return render(request, 'ramal.html', dados)

@login_required(login_url='/login/')
def submit_edicao(request):
    if request.POST:
        ramal = request.POST.get('ramal')
        responsavel= request.POST.get('responsavel')
        email=request.POST.get('email')
        #setor=request.POST.get('setor')
        #empresa=request.POST.get('empresa')
        id_setor = Setores.objects.filter(pk='pk_setor')
        id_empresa = Empresas.objects.filter(pk='pk_empresa')
        Ramais.objects.create(ramal=ramal,
                              nome_resp=responsavel,
                              email=email,
                              setor_ramais=id_setor,
                              empresa_ramais=id_empresa)
    return redirect('/ramais/edicao/')

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