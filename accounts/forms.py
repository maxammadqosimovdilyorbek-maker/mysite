
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            "placeholder": "email@example.com",
            "autocomplete": "email",
        }),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Foydalanuvchi nomi",
        }
        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "username",
                "autocomplete": "username",
            }),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Bu email allaqachon ro'yxatdan o'tgan."
            )
        return email

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "project_type",
            "design",
            "description",
            "features",
        ]
        labels = {
            "name": "Loyiha nomi",
            "project_type": "Loyiha turi",
            "design": "Dizayn uslubi",
            "description": "Loyiha haqida",
            "features": "Kerakli funksiyalar",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Masalan: DiliShop",
                "maxlength": "100",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Loyihangiz nima vazifa bajaradi?",
                "rows": 4,
            }),
            "features": forms.TextInput(attrs={
                "placeholder": "Login, profil, qidiruv, chat...",
                "maxlength": "500",
            }),
        }

