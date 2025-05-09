# Generated by Django 5.1.7 on 2025-03-29 04:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherapplication',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacherlanguage', verbose_name='Язык обучения'),
        ),
        migrations.AddField(
            model_name='teacherapplication',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teacherapplication',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teachingmaterial',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.teacherlanguage', verbose_name='Язык'),
        ),
        migrations.AddField(
            model_name='teachingmaterial',
            name='shared_with',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_teacher': False}, related_name='received_materials', to=settings.AUTH_USER_MODEL, verbose_name='Ученики, которым передан материал'),
        ),
        migrations.AddField(
            model_name='teachingmaterial',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'is_teacher': True}, on_delete=django.db.models.deletion.CASCADE, related_name='materials', to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='teachingmaterialfile',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='main.teachingmaterial', verbose_name='Материал'),
        ),
    ]
