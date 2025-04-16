from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect

from .models import TeacherRequest


@staff_member_required
def handle_teacher_request(request, request_id, action):
    req = get_object_or_404(TeacherRequest, pk=request_id)
    
    if action == 'approve':
        req.approved = True
        req.save()
        req.user.is_teacher = True
        req.user.save()
    elif action == 'reject':
        req.approved = True
        req.save()

    return redirect('users:staff_panel')
