from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from app import views


urlpatterns = [
    # Administração
    path(
        "admin/",
        admin.site.urls,
        name="admin",
    ),

    # Página inicial
    path(
        "",
        RedirectView.as_view(
            url="/ramais/",
            permanent=False,
        ),
        name="home",
    ),

    # Ramais
    path(
        "ramais/",
        views.lista_ramais,
        name="lista_ramais",
    ),

    path(
        "ramais/edicao/",
        views.ed_ramal,
        name="edicao_ramal",
    ),

    path(
        "ramais/edicao/submit/",
        views.submit_edicao,
        name="submit_edicao",
    ),

    path(
        "ramais/edicao/setor/",
        views.add_setor,
        name="add_setor",
    ),

    path(
        "ramais/edicao/setor/submit/",
        views.submit_setor,
        name="submit_setor",
    ),

    path(
        "delete/<int:id_ramal>/",
        views.delete_ramal,
        name="delete_ramal",
    ),

    # Emails
    path(
        "emails/",
        views.lista_emails,
        name="lista_emails",
    ),

    path(
        "emails/edicao/",
        views.ed_ramal,
        name="edicao_email",
    ),

    path(
        "emails/edicao/submit/",
        views.submit_edicao,
        name="submit_edicao_email",
    ),

    path(
        "emails/delete/<int:id_ramal>/",
        views.delete_email,
        name="delete_email",
    ),

    # Empresas
    path(
        "empresas/",
        views.lista_empresas,
        name="lista_empresas",
    ),

    # Autenticação
    path(
        "login/",
        views.login_edicao,
        name="login",
    ),

    path(
        "login/submit/",
        views.submit_login,
        name="submit_login",
    ),

    path(
        "logout/",
        views.logout_edicao,
        name="logout",
    ),

    # API
    path(
        "api/",
        include("app.urls"),
    ),
]