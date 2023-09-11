from django.shortcuts import render
from django.http import FileResponse
from .models import TeamMember


def about_us(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about_app/AboutUs.html', context={'team_members': team_members})


def vita_download(request, id):
    member = TeamMember.objects.get(id=id)
    pdf_file = member.pdf_file

    response = FileResponse(pdf_file)
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'

    return response
