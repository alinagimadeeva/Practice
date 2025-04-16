from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView, TemplateView
from .forms import (CustomPasswordChangeForm, TeacherLanguageForm,
                         TeacherProfileForm, UserPhotoFormSet,
                         UserRegistrationForm, UserUpdateForm)
from .models import (TeacherLanguage, TeacherProfile, TeacherRequest,
                          UserPhoto)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_form'] = UserUpdateForm(instance=user)

        teacher_request = TeacherRequest.objects.filter(user=user).first()
        print(f'teacher_request {teacher_request}')
        context['teacher_request'] = teacher_request

        if user.is_teacher:
            profile, _ = TeacherProfile.objects.get_or_create(user=user)
            context['teacher_form'] = TeacherProfileForm(instance=profile)

            LanguageFormSet = modelformset_factory(
                TeacherLanguage, form=TeacherLanguageForm, extra=1, can_delete=True)
            context['language_formset'] = LanguageFormSet(
                queryset=TeacherLanguage.objects.filter(profile=profile),
                prefix='languages'
            )

        context['photo_formset'] = UserPhotoFormSet(
            queryset=UserPhoto.objects.filter(user=user),
            prefix='photos'
        )

        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        context = self.get_context_data()

        user_form = UserUpdateForm(request.POST, instance=user)
        context['user_form'] = user_form

        photo_formset = UserPhotoFormSet(
            request.POST,
            request.FILES,
            queryset=UserPhoto.objects.filter(user=user),
            prefix='photos'
        )
        context['photo_formset'] = photo_formset

        is_valid = user_form.is_valid() and photo_formset.is_valid()

        teacher_form = None
        language_formset = None
        language_formset_has_duplicates = False

        if user.is_teacher:
            profile, _ = TeacherProfile.objects.get_or_create(user=user)
            teacher_form = TeacherProfileForm(request.POST, instance=profile)
            LanguageFormSet = modelformset_factory(
                TeacherLanguage, form=TeacherLanguageForm, extra=1, can_delete=True)
            language_formset = LanguageFormSet(
                request.POST,
                queryset=TeacherLanguage.objects.filter(profile=profile),
                prefix='languages'
            )

            context['teacher_form'] = teacher_form
            context['language_formset'] = language_formset

            # Валидируем и проверяем на дубликаты
            teacher_valid = teacher_form.is_valid()
            language_valid = language_formset.is_valid()

            if language_valid:
                seen_languages = set()
                for form in language_formset:
                    if not form.cleaned_data.get('DELETE', False):
                        lang = form.cleaned_data.get('language')
                        if lang in seen_languages:
                            form.add_error('language', 'Этот язык уже добавлен.')
                            language_formset_has_duplicates = True
                        else:
                            seen_languages.add(lang)

            is_valid &= teacher_valid and language_valid and not language_formset_has_duplicates

        if is_valid:
            user_form.save()

            photo_formset.instance = user
            for photo in photo_formset.save(commit=False):
                photo.user = user
                photo.save()
            for obj in photo_formset.deleted_objects:
                obj.delete()

            if user.is_teacher:
                teacher_form.save()
                langs = language_formset.save(commit=False)
                for lang in langs:
                    lang.profile = profile
                    lang.save()
                for obj in language_formset.deleted_objects:
                    obj.delete()

            return redirect('users:profile')

        return self.render_to_response(context)



@method_decorator(staff_member_required, name='dispatch')
class StaffPanelView(TemplateView):
    template_name = 'staff_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_requests'] = TeacherRequest.objects.filter(
            approved=False)
        return context


def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:index')
        else:
            error_message = 'Неверный логин или пароль.'

    return render(request, 'users/login.html', {'error_message': error_message})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # вот здесь важно — получаем cleaned_data из формы
            if form.cleaned_data.get('is_teacher_request'):
                TeacherRequest.objects.create(user=user)

            return redirect('main:index')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class PasswordChangeView(FormView):
    template_name = 'users/password_change.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('users:profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main:index')
