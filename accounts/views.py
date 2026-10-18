
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


def home(request):
    return render(request, "accounts/home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Akkauntingiz muvaffaqiyatli yaratildi!"
            )
            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(
        request, "accounts/register.html", {"form": form}
    )


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")


@login_required
def profile(request):
    return render(request, "accounts/profile.html")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

@login_required
def studio(request):
    projects = Project.objects.filter(owner=request.user)
    return render(
        request,
        "accounts/studio.html",
        {"projects": projects},
    )


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(
                request, "Loyihangiz muvaffaqiyatli saqlandi!"
            )
            return redirect("project_detail", pk=project.pk)
    else:
        form = ProjectForm()

    return render(
        request,
        "accounts/project_form.html",
        {"form": form},
    )


@login_required
def project_detail(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user,
    )
    return render(
        request,
        "accounts/project_detail.html",
        {"project": project},
    )


@login_required
def project_delete(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        project.delete()
        messages.success(request, "Loyiha o‘chirildi.")
        return redirect("studio")

    return redirect("project_detail", pk=project.pk)


