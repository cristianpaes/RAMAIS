from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from rest_framework import viewsets

from app.models import Empresas, Ramais, Setores
from app.serializers import RamaisSerializer


class ramaisViewSet(viewsets.ModelViewSet):
    queryset = Ramais.objects.all().order_by('ramal')
    serializer_class = RamaisSerializer


def lista_ramais(request):
    """
    Lista os ramais com suporte a pesquisa e paginação.
    """

    busca = request.GET.get('search', '').strip()

    ramais = Ramais.objects.all().order_by('ramal')

    if busca:
        setores = Setores.objects.filter(
            setor__icontains=busca
        )

        ramais = ramais.filter(
            Q(ramal__icontains=busca)
            | Q(nome_resp__icontains=busca)
            | Q(setor_ramais__in=setores)
        )

    paginator = Paginator(ramais, 5)

    page_number = request.GET.get('page')
    pagina = paginator.get_page(page_number)

    return render(
        request,
        'ramais.html',
        {'ramais': pagina}
    )


def lista_emails(request):
    """
    Lista os emails com suporte a pesquisa e paginação.
    """

    busca = request.GET.get('search', '').strip()

    emails = Ramais.objects.all().order_by('nome_resp')

    if busca:
        setores = Setores.objects.filter(
            setor__icontains=busca
        )

        emails = emails.filter(
            Q(nome_resp__icontains=busca)
            | Q(setor_ramais__in=setores)
        )

    paginator = Paginator(emails, 5)

    page_number = request.GET.get('page')
    pagina = paginator.get_page(page_number)

    return render(
        request,
        'emails.html',
        {'emails': pagina}
    )


def lista_empresas(request):
    """
    Lista todas as empresas cadastradas.
    """

    empresas = Empresas.objects.all().order_by('nome_emp')

    return render(
        request,
        'empresas.html',
        {'empresas': empresas}
    )


def login_edicao(request):
    """
    Exibe a tela de login.
    """

    return render(request, 'login.html')


@require_POST
def submit_login(request):
    """
    Processa a autenticação do usuário.
    """

    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')

    if not username or not password:
        messages.error(
            request,
            'Informe usuário e senha.'
        )

        return redirect('login')

    usuario = authenticate(
        request,
        username=username,
        password=password
    )

    if usuario is not None:
        login(request, usuario)

        return redirect('lista_ramais')

    messages.error(
        request,
        'Usuário ou senha inválido.'
    )

    return redirect('login')


def logout_edicao(request):
    """
    Encerra a sessão do usuário.
    """

    logout(request)

    return redirect('home')


@login_required(login_url='/login/')
def ed_ramal(request):
    """
    Exibe o formulário para cadastrar ou editar um ramal.
    """

    id_ramal = request.GET.get('id')

    setores = Setores.objects.all().order_by('setor')
    empresas = Empresas.objects.all().order_by('nome_emp')

    dados = {
        'setores': setores,
        'empresas': empresas
    }

    if id_ramal:
        dados['ramais'] = get_object_or_404(
            Ramais,
            id=id_ramal
        )

    return render(
        request,
        'ramal.html',
        dados
    )


@login_required(login_url='/login/')
@require_POST
def submit_edicao(request):
    """
    Cria ou atualiza um ramal.
    """

    ramal = request.POST.get('ramal', '').strip()
    responsavel = request.POST.get('responsavel', '').strip()
    email = request.POST.get('email', '').strip()

    setor_id = request.POST.get('setor')
    empresa_id = request.POST.get('empresa')
    id_ramal = request.POST.get('id_ramal')

    if not ramal or not responsavel or not email:
        messages.error(
            request,
            'Preencha todos os campos obrigatórios.'
        )

        return redirect('edicao_ramal')

    if not setor_id or not empresa_id:
        messages.error(
            request,
            'Selecione o setor e a empresa.'
        )

        return redirect('edicao_ramal')

    setor = get_object_or_404(
        Setores,
        id=setor_id
    )

    empresa = get_object_or_404(
        Empresas,
        id=empresa_id
    )

    if id_ramal:

        registro = get_object_or_404(
            Ramais,
            id=id_ramal
        )

        registro.ramal = ramal
        registro.nome_resp = responsavel
        registro.email = email
        registro.setor_ramais = setor
        registro.empresa_ramais = empresa

        registro.save()

        messages.success(
            request,
            'Ramal atualizado com sucesso.'
        )

    else:

        Ramais.objects.create(
            ramal=ramal,
            nome_resp=responsavel,
            email=email,
            setor_ramais=setor,
            empresa_ramais=empresa
        )

        messages.success(
            request,
            'Ramal cadastrado com sucesso.'
        )

    return redirect('lista_ramais')


@login_required(login_url='/login/')
def add_setor(request):
    """
    Exibe o formulário para cadastro de setor.
    """

    return render(
        request,
        'setor.html'
    )


@login_required(login_url='/login/')
@require_POST
def submit_setor(request):
    """
    Cadastra um novo setor.
    """

    setor = request.POST.get('setor', '').strip()

    if not setor:
        messages.error(
            request,
            'Informe o nome do setor.'
        )

        return redirect('add_setor')

    if Setores.objects.filter(
        setor__iexact=setor
    ).exists():

        messages.error(
            request,
            f'O setor "{setor}" já está cadastrado.'
        )

        return redirect('add_setor')

    Setores.objects.create(
        setor=setor
    )

    messages.success(
        request,
        f'Setor "{setor}" cadastrado com sucesso.'
    )

    return redirect('edicao_ramal')


@login_required(login_url='/login/')
@require_POST
def delete_ramal(request, id_ramal):
    """
    Exclui somente o registro de Ramais.
    """

    registro = get_object_or_404(
        Ramais,
        id=id_ramal
    )

    registro.delete()

    messages.success(
        request,
        'Ramal excluído com sucesso.'
    )

    return redirect('lista_ramais')


@login_required(login_url='/login/')
@require_POST
def delete_email(request, id_ramal):
    """
    Exclui somente o registro de Ramais associado ao email.
    """

    registro = get_object_or_404(
        Ramais,
        id=id_ramal
    )

    registro.delete()

    messages.success(
        request,
        'Email excluído com sucesso.'
    )

    return redirect('lista_emails')