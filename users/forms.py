from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class UserRegisterForm(UserCreationForm):
    """Регистрация пользователя"""

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')  # пользователя просят ввести 2 раза пароль

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы регистрации"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['email'].widget.attrs.update({"placeholder": 'Введите свой email'})
            self.fields['password1'].widget.attrs.update({"placeholder": 'Придумайте свой пароль'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Повторите придуманный пароль'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class UserProfileForm(UserChangeForm):
    """Класс профиль"""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы профиль"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['email'].widget.attrs.update({"placeholder": 'Введите свой email'})
            self.fields['first_name'].widget.attrs.update({"placeholder": 'Ваше имя'})
            self.fields["last_name"].widget.attrs.update({"placeholder": 'Ваша фамилия'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})
            self.fields['password'].widget = forms.HiddenInput()  # убирает поле пароль


class UserForgotPasswordForm(PasswordResetForm):
    """Запрос на восстановление пароля"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """Изменение пароля пользователя после подтверждения"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
