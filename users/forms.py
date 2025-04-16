import re

import phonenumbers
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from phonenumber_field.formfields import PhoneNumberField
from .models import Language, TeacherLanguage, TeacherProfile, UserPhoto

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите пароль'})
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Телефон*',
            'required': True,
            'autocomplete': 'phone'})
    )
    is_teacher_request = forms.BooleanField(
        required=False,
        label="Хочу быть преподавателем",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль*',
                'autocomplete': 'new-password'}),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин*',
                'required': True}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя*',
                'required': True,
                'autocomplete': 'first_name'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша фамилия',
                'autocomplete': 'last_name'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail*',
                'autocomplete': 'email',
                'id': 'id_email_2'}),
        }

    def clean_phone(self):
        """Приводит телефон к единому формату и проверяет уникальность"""
        phone = self.cleaned_data.get("phone")
        if not phone:
            raise ValidationError("Введите номер телефона.")

        if isinstance(phone, phonenumbers.PhoneNumber):
            phone = phonenumbers.format_number(
                phone, phonenumbers.PhoneNumberFormat.E164)
        else:
            phone = re.sub(r'\D', '', phone)

            if phone.startswith("8") and len(phone) == 11:
                phone = "+7" + phone[1:]
            elif phone.startswith("7") and len(phone) == 11:
                phone = "+7" + phone[1:]
            elif phone.startswith("+7") and len(phone) == 12:
                pass
            else:
                try:
                    parsed_phone = phonenumbers.parse(
                        phone, "RU")
                    if not phonenumbers.is_valid_number(parsed_phone):
                        raise ValidationError("Некорректный номер телефона.")
                    phone = phonenumbers.format_number(
                        parsed_phone, phonenumbers.PhoneNumberFormat.E164)
                except phonenumbers.NumberParseException:
                    raise ValidationError("Некорректный номер телефона.")

        # Проверяем уникальность
        if User.objects.filter(phone=phone).exists():
            raise ValidationError(
                "Пользователь с таким телефоном уже существует.")

        return phone

    def clean_password_repeat(self):
        """Проверка совпадения паролей"""
        password = self.cleaned_data.get("password")
        password_repeat = self.cleaned_data.get("password_repeat")
        if password and password_repeat and password != password_repeat:
            raise ValidationError("Пароли не совпадают.")
        return password_repeat

    def clean(self):
        """Кастомная проверка уникальности логина и почты"""
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if User.objects.filter(username=username).exists():
            self.add_error(
                'username', 'Пользователь с таким именем уже существует.')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', 'Пользователь с таким Email уже существует.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Старый пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Введите старый пароль'}),
    )
    new_password1 = forms.CharField(
        label="Новый пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Введите новый пароль'}),
    )
    new_password2 = forms.CharField(
        label="Подтвердите пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Подтвердите пароль'}),
    )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'middle_name', 'last_name', 'email', 'phone']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs.get('instance')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if username and User.objects.exclude(pk=self.user.pk).filter(username=username).exists():
            self.add_error(
                'username', 'Пользователь с таким логином уже существует.')

        if email and User.objects.exclude(pk=self.user.pk).filter(email=email).exists():
            self.add_error(
                'email', 'Пользователь с таким email уже существует.')

        if phone and User.objects.exclude(pk=self.user.pk).filter(phone=phone).exists():
            self.add_error(
                'phone', 'Пользователь с таким телефоном уже существует.')

        return cleaned_data


class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['bio', 'experience']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TeacherLanguageForm(forms.ModelForm):
    class Meta:
        model = TeacherLanguage
        fields = ['language', 'price_per_hour']
        widgets = {
            'language': forms.Select(attrs={'class': 'form-select'}),
            'price_per_hour': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['image', 'order']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width:100px'}),
        }


UserPhotoFormSet = modelformset_factory(
    UserPhoto,
    form=UserPhotoForm,
    extra=1,
    can_delete=True
)
