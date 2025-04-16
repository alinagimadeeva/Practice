from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Exists, OuterRef, Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from .forms import TeachingMaterialFileFormSet, TeachingMaterialForm
from .models import (TeacherApplication, TeachingMaterial,
                         TeachingMaterialFile)
from users.models import TeacherLanguage, TeacherRequest, User


class StudentProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'main/student_profile.html'
    context_object_name = 'student'

    def get_queryset(self):
        return User.objects.filter(is_teacher=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        teacher = self.request.user

        # Проверяем, есть ли принятая заявка от этого студента
        is_my_student = TeacherApplication.objects.filter(
            teacher=teacher,
            student=student,
            status=TeacherApplication.Status.ACCEPTED
        ).exists()

        context['is_my_student'] = is_my_student
        return context


class MyStudentsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = TeacherApplication
    template_name = 'main/my_students.html'
    context_object_name = 'applications'

    def test_func(self):
        return self.request.user.is_teacher

    def get_queryset(self):
        return TeacherApplication.objects.filter(
            teacher=self.request.user,
            status=TeacherApplication.Status.ACCEPTED
        ).select_related('student', 'language')


@login_required
def request_teacher_status(request):
    teacher_request, created = TeacherRequest.objects.get_or_create(
        user=request.user)

    if not created and teacher_request.approved:
        return redirect('main:index')  # Уже одобрен

    if request.method == 'POST':
        if teacher_request.approved is False:
            teacher_request.approved = None
            teacher_request.save()
        return redirect('main:index')

    return redirect('users:profile')


class StudentMaterialsView(LoginRequiredMixin, ListView):
    template_name = 'main/student_materials.html'
    context_object_name = 'materials'

    def get_queryset(self):
        return TeachingMaterial.objects.filter(
            shared_with=self.request.user).select_related(
                'teacher', 'language__language').prefetch_related('files')


class TeacherMaterialsView(LoginRequiredMixin, TemplateView):
    template_name = 'main/teacher_materials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        materials = TeachingMaterial.objects.filter(
            teacher=self.request.user
        ).select_related('language__language').prefetch_related('files')

        accepted_apps = TeacherApplication.objects.filter(
            teacher=self.request.user,
            status=TeacherApplication.Status.ACCEPTED
        ).select_related('student', 'language__language')

        students_by_language = {}
        for app in accepted_apps:
            lang_id = app.language_id
            if app.student not in students_by_language.get(lang_id, []):
                students_by_language.setdefault(
                    lang_id, []).append(app.student)

        materials_with_students = []
        for material in materials:
            students = students_by_language.get(material.language_id, [])
            materials_with_students.append({
                'material': material,
                'students': students
            })

        context['materials_with_students'] = materials_with_students
        return context


class CreateTeachingMaterialView(LoginRequiredMixin, CreateView):
    model = TeachingMaterial
    form_class = TeachingMaterialForm
    template_name = 'main/create_material.html'
    success_url = reverse_lazy('main:teacher_materials')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file_formset = TeachingMaterialFileFormSet(
            self.request.POST or None,
            self.request.FILES or None,
            prefix='files',
            queryset=TeachingMaterialFile.objects.none()
        )
        context['file_formset'] = file_formset
        context['empty_form'] = file_formset.empty_form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        file_formset = context['file_formset']

        if file_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.teacher = self.request.user
            self.object.save()

            files = file_formset.save(commit=False)
            for file in files:
                file.material = self.object
                file.save()
            return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(form=form))


class ShareMaterialView(LoginRequiredMixin, View):
    def post(self, request, material_id):
        material = get_object_or_404(
            TeachingMaterial, id=material_id, teacher=request.user)
        student_id = request.POST.get('student_id')
        student = get_object_or_404(User, id=student_id)
        material.shared_with.add(student)
        return redirect('main:teacher_materials')


class TeacherApplicationsView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        ListView):
    model = TeacherApplication
    template_name = 'main/teacher_applications.html'
    context_object_name = 'applications'

    def test_func(self):
        return self.request.user.is_teacher

    def get_queryset(self):
        return (
            TeacherApplication.objects.filter(
                teacher=self.request.user, status='pending')
            .select_related('student', 'language')
        )


class UpdateApplicationStatusView(View):
    def get(self, request, pk, action):
        app = get_object_or_404(
            TeacherApplication, pk=pk, teacher=request.user)

        if action == "approve":
            app.status = "accepted"
            messages.success(
                request, f"Заявка {app.student.get_full_name} принята.")
        elif action == "reject":
            app.status = "rejected"
            messages.warning(
                request, f"Заявка {app.student.get_full_name} отклонена.")
        else:
            messages.error(request, "Некорректное действие.")

        app.save()
        return redirect('main:teacher_applications')


class MyApplicationsView(ListView):
    template_name = "main/my_applications.html"
    context_object_name = "teachers"

    def get_queryset(self):
        # Получаем преподавателей, которым отправляли заявки
        return User.objects.filter(
            is_teacher=True,
            applications_received__student=self.request.user
        ).distinct().prefetch_related("teacher_profile__language_prices")


class ApplyToTeacherView(LoginRequiredMixin, View):
    def post(self, request, pk):
        teacher = get_object_or_404(User, pk=pk, is_teacher=True)
        language_id = request.POST.get('language')
        message = request.POST.get('message', '')

        # запретить отправку себе
        if teacher == request.user:
            return redirect('main:teacher_profile', pk=pk)

        # проверяем, есть ли уже активная или принятая заявка
        exists = TeacherApplication.objects.filter(
            teacher=teacher,
            student=request.user,
            language_id=language_id,
            status__in=[
                TeacherApplication.Status.PENDING,
                TeacherApplication.Status.ACCEPTED
            ]
        ).exists()

        if not exists:
            TeacherApplication.objects.create(
                teacher=teacher,
                student=request.user,
                language_id=language_id,
                message=message
            )
        return redirect('main:teacher_profile', pk=pk)


class TeacherDetailView(DetailView):
    model = User
    template_name = 'main/teacher_detail.html'
    context_object_name = 'teacher'

    def get_queryset(self):
        return User.objects.filter(is_teacher=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            applications = teacher.applications_received.filter(
                student=user).select_related('language')
            accepted_lang_ids = applications.filter(
                status='accepted').values_list('language_id', flat=True)
            context['user_applications'] = applications.order_by('-created_at')
            context['existing_application'] = applications.filter(
                status='pending').first()
            context['available_languages'] = teacher.teacher_profile.language_prices.exclude(
                id__in=accepted_lang_ids)
        else:
            context['available_languages'] = teacher.teacher_profile.language_prices.all()

        return context


class TeacherListView(ListView):
    model = User
    template_name = 'main/teachers_list.html'
    context_object_name = 'teachers'
    paginate_by = 12

    def get_queryset(self):
        # Только у кого есть профиль
        base_qs = User.objects.filter(
            is_teacher=True, teacher_profile__isnull=False)

        # Ограничим только тех, у кого:
        # - есть bio ИЛИ опыт
        # - есть хотя бы 1 язык с ценой
        valid_profiles = base_qs.annotate(
            has_languages=Exists(
                TeacherLanguage.objects.filter(profile__user=OuterRef('pk'))
            )
        ).filter(
            Q(teacher_profile__bio__isnull=False) | Q(
                teacher_profile__experience__isnull=False),
            has_languages=True
        )

        return valid_profiles.select_related(
            'teacher_profile').prefetch_related(
                'teacher_profile__language_prices__language')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = User.objects.filter(
            is_teacher=True
        ).prefetch_related('photos')[:4]
        return context
