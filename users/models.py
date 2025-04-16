from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    is_teacher = models.BooleanField('Преподаватель?', default=False)
    phone = PhoneNumberField(
        'Телефон',
        null=True, blank=True, unique=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    is_active = models.BooleanField('Доступ в ЛК', default=True)
    middle_name = models.CharField('Отчество', max_length=150, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()


class TeacherRequest(models.Model):
    user = models.OneToOneField(
        'users.User', on_delete=models.CASCADE, related_name='teacher_request')
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Заявка от {self.user.username}"


class Language(models.Model):
    name = models.CharField('Язык', max_length=100, unique=True)

    def __str__(self):
        return self.name


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher_profile')
    bio = models.TextField('О себе', blank=True)
    experience = models.PositiveIntegerField(
        'Опыт (с какого года)', null=True, blank=True)

    def __str__(self):
        return f"Профиль препода: {self.user.username}"

    def get_experience(self):
        current_year = now().year
        years = max(0, current_year - self.experience)
        return f"{years} {self._decline_years(years)}"

    def _decline_years(self, years):
        if 11 <= years % 100 <= 19:
            return "лет"
        last_digit = years % 10
        if last_digit == 1:
            return "год"
        elif 2 <= last_digit <= 4:
            return "года"
        else:
            return "лет"


class TeacherLanguage(models.Model):
    profile = models.ForeignKey(
        TeacherProfile, on_delete=models.CASCADE, related_name='language_prices')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    price_per_hour = models.DecimalField(
        'Цена за час', max_digits=6, decimal_places=0)

    class Meta:
        unique_together = ('profile', 'language')

    def __str__(self):
        return f"{self.profile.user.username} — {self.language.name} ({self.price_per_hour}₽)"


class UserPhoto(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    image = models.ImageField('Фото', upload_to='user_photos/')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Фото пользователя {self.user.username}"
