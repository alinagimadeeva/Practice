from django.contrib import admin
from .models import (TeacherApplication, TeachingMaterial,
                         TeachingMaterialFile)


class TeachingMaterialFileInline(admin.TabularInline):
    model = TeachingMaterialFile
    extra = 1


@admin.register(TeachingMaterial)
class TeachingMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'created_at')
    search_fields = ('title', 'teacher__email', 'teacher__first_name')
    list_filter = ('created_at',)
    inlines = [TeachingMaterialFileInline]


@admin.register(TeacherApplication)
class TeacherApplicationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'created_at')
    list_filter = ('created_at', 'teacher')
    search_fields = ('student__username', 'teacher__username')
