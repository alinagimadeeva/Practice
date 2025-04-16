from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers_list'),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(),
         name='teacher_profile'),
    path('teacher/<int:pk>/apply/',
         views.ApplyToTeacherView.as_view(), name='apply_to_teacher'),
    path('my-applications/', views.MyApplicationsView.as_view(),
         name='my_applications'),
    path('applications/', views.TeacherApplicationsView.as_view(),
         name='teacher_applications'),
    path('update_application_status/<int:pk>/<str:action>/',
         views.UpdateApplicationStatusView.as_view(),
         name='update_application_status'),
    path('materials/', views.TeacherMaterialsView.as_view(),
         name='teacher_materials'),
    path('materials/create/', views.CreateTeachingMaterialView.as_view(),
         name='create_material'),
    path('materials/share/<int:material_id>/',
         views.ShareMaterialView.as_view(), name='share_material'),
    path('user-materials/', views.StudentMaterialsView.as_view(),
         name='student_materials'),
    path('teacher/request/', views.request_teacher_status,
         name='request_teacher_status'),
    path('my-student/', views.MyStudentsView.as_view(), name='my_student'),
    path('student/<int:pk>/', views.StudentProfileView.as_view(),
         name='student_profile'),


]
