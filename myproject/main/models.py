from django.db import models
from users.models import Language, TeacherLanguage, User


class TeacherApplication(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Ожидает'
        ACCEPTED = 'accepted', 'Принята'
        REJECTED = 'rejected', 'Отклонена'

    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='applications_received')
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='applications_sent')
    language = models.ForeignKey('users.TeacherLanguage', on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='Язык обучения')
    message = models.TextField('Сообщение ученика', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        'Статус',
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )

    class Meta:
        verbose_name = 'Заявка на обучение'
        verbose_name_plural = 'Заявки на обучение'

    def __str__(self):
        return f"{self.student.get_full_name()} → {self.teacher.get_full_name()}"


class TeachingMaterial(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='materials',
        limit_choices_to={'is_teacher': True},
        verbose_name='Преподаватель'
    )
    title = models.CharField('Название материала', max_length=255)
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(
        User,
        blank=True,
        related_name='received_materials',
        verbose_name='Ученики, которым передан материал',
        limit_choices_to={'is_teacher': False}
    )
    language = models.ForeignKey(
        TeacherLanguage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Язык'
    )

    class Meta:
        verbose_name = 'Учебный материал'
        verbose_name_plural = 'Учебные материалы'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TeachingMaterialFile(models.Model):
    material = models.ForeignKey(
        TeachingMaterial, on_delete=models.CASCADE, related_name='files',
        verbose_name='Материал'
    )
    file = models.FileField('Файл', upload_to='teaching_materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Файл материала'
        verbose_name_plural = 'Файлы материалов'

    def __str__(self):
        return self.file.name
