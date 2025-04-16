# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TeacherProfile, TeacherRequest, User, UserPhoto


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('id', 'username', 'email', 'phone', 'is_teacher', 'is_active', 'is_staff')
    list_filter = ('is_teacher', 'is_active', 'is_staff')
    list_editable = ('is_teacher', 'is_active')
    search_fields = ('username', 'email', 'phone')

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительные поля', {
            'fields': ('phone', 'is_teacher')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('phone', 'is_teacher'),
        }),
    )


@admin.register(TeacherRequest)
class TeacherRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'approved')
    list_filter = ('approved',)
    actions = ['approve_requests']

    @admin.action(description='✅ Одобрить выбранные заявки и выдать статус преподавателя')
    def approve_requests(self, request, queryset):
        updated = 0
        for req in queryset:
            if not req.approved:
                req.approved = True
                req.save()
                user = req.user
                user.is_teacher = True
                user.save()
                updated += 1
        self.message_user(request, f"✅ Одобрено и назначено преподавателей: {updated}")


@admin.register(UserPhoto)
class UserPhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'order')
    list_filter = ('user',)
    ordering = ('user', 'order')


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)
    ordering = ('user',)