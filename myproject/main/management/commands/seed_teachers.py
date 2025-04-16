# main/management/commands/seed_teachers.py

import os
import random

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from main.models import (TeacherApplication, TeachingMaterial,
                         TeachingMaterialFile)
from users.models import (Language, TeacherLanguage, TeacherProfile, User,
                          UserPhoto)


class Command(BaseCommand):
    help = 'Создание тестовых преподавателей, учеников, заявок и материалов'

    def handle(self, *args, **options):
        languages = [
            'Английский', 'Французский', 'Немецкий', 'Испанский',
            'Итальянский', 'Китайский', 'Японский'
        ]
        language_objs = {}
        for name in languages:
            lang, _ = Language.objects.get_or_create(name=name)
            language_objs[name] = lang
        self.stdout.write(self.style.SUCCESS("Языки добавлены."))

        # # 2. Преподаватели
        # teacher_data = [
        #     {'first_name': 'Алексей', 'last_name': 'Петров', 'email': 'aleksey@example.com'},
        #     {'first_name': 'Юрий', 'last_name': 'Иванов', 'email': 'yuri@example.com'},
        #     {'first_name': 'Сергей', 'last_name': 'Смирнов', 'email': 'sergey@example.com'},
        #     {'first_name': 'Елена', 'last_name': 'Николаева', 'email': 'elena@example.com'},
        # ]
        #
        # photos_dir = os.path.join(settings.MEDIA_ROOT, 'test_foto')
        # photo_files = sorted(os.listdir(photos_dir))[:4]
        # teachers = []
        #
        # for i, data in enumerate(teacher_data):
        #     teacher, created = User.objects.get_or_create(
        #         email=data['email'],
        #         defaults={
        #             'username': data['email'],
        #             'is_teacher': True,
        #             'first_name': data['first_name'],
        #             'last_name': data['last_name'],
        #         }
        #     )
        #     if created:
        #         teacher.set_password('test1234')
        #         teacher.save()
        #
        #     profile, _ = TeacherProfile.objects.get_or_create(
        #         user=teacher, defaults={'experience': 2015 + i})
        #
        #     existing_langs = set(
        #         profile.language_prices.values_list('language_id', flat=True))
        #     langs_for_teacher = random.sample(list(language_objs.values()), k=2)
        #     for lang in langs_for_teacher:
        #         if lang.id not in existing_langs:
        #             TeacherLanguage.objects.get_or_create(
        #                 profile=profile,
        #                 language=lang,
        #                 defaults={'price_per_hour': 1000 + i * 200}
        #             )
        #
        #     if not teacher.photos.exists() and i < len(photo_files):
        #         photo_path = os.path.join(photos_dir, photo_files[i])
        #         with open(photo_path, 'rb') as img:
        #             file = File(img)
        #             file.name = os.path.basename(photo_path)
        #             UserPhoto.objects.create(user=teacher, image=file, order=0)
        #
        #     teachers.append(teacher)
        # self.stdout.write(self.style.SUCCESS("Преподаватели созданы."))
        #
        # # 3. Ученики
        # student_data = [
        #     {'first_name': 'Иван', 'last_name': 'Орлов', 'email': 'ivan@example.com'},
        #     {'first_name': 'Анна', 'last_name': 'Соколова', 'email': 'anna@example.com'},
        #     {'first_name': 'Никита', 'last_name': 'Кузнецов', 'email': 'nikita@example.com'},
        #     {'first_name': 'Ольга', 'last_name': 'Федорова', 'email': 'olga@example.com'},
        # ]
        #
        # students = []
        # for data in student_data:
        #     student, created = User.objects.get_or_create(
        #         email=data['email'],
        #         defaults={
        #             'username': data['email'],
        #             'is_teacher': False,
        #             'first_name': data['first_name'],
        #             'last_name': data['last_name'],
        #         }
        #     )
        #     if created:
        #         student.set_password('test1234')
        #         student.save()
        #     students.append(student)
        # self.stdout.write(self.style.SUCCESS("Ученики созданы."))
        #
        # # 4. Заявки
        # for student in students:
        #     for _ in range(2):
        #         teacher = random.choice(teachers)
        #         langs = teacher.teacher_profile.language_prices.all()
        #         if not langs:
        #             continue
        #         lang = random.choice(langs)
        #         TeacherApplication.objects.get_or_create(
        #             teacher=teacher,
        #             student=student,
        #             language=lang,
        #             defaults={'status': TeacherApplication.Status.ACCEPTED}
        #         )
        # self.stdout.write(self.style.SUCCESS("Заявки созданы."))
        #
        # # 5. Материалы
        # files_dir = os.path.join(settings.MEDIA_ROOT, 'test_materials')
        # if not os.path.exists(files_dir):
        #     os.makedirs(files_dir)
        #     for i in range(4):
        #         with open(os.path.join(files_dir, f'material_{i+1}.txt'), 'w') as f:
        #             f.write(f'Это файл учебного материала #{i+1}.')
        #
        # files = sorted(os.listdir(files_dir))
        #
        # for i, teacher in enumerate(teachers):
        #     langs = teacher.teacher_profile.language_prices.all()
        #     if not langs:
        #         continue
        #     lang = langs.first()
        #     mat, _ = TeachingMaterial.objects.get_or_create(
        #         teacher=teacher,
        #         title=f"Материал по {lang.language.name}",
        #         defaults={
        #             'description': "Немного базовой информации",
        #             'language': lang
        #         }
        #     )
        #
        #     if not mat.files.exists():
        #         file_path = os.path.join(files_dir, files[i % len(files)])
        #         with open(file_path, 'rb') as f:
        #             file = File(f)
        #             file.name = os.path.basename(file_path)
        #             TeachingMaterialFile.objects.create(material=mat, file=file)
        #
        #     accepted_apps = TeacherApplication.objects.filter(
        #         teacher=teacher,
        #         status=TeacherApplication.Status.ACCEPTED,
        #         language=lang
        #     )
        #     for app in accepted_apps:
        #         mat.shared_with.add(app.student)
        #
        # self.stdout.write(self.style.SUCCESS("Материалы добавлены и розданы."))
