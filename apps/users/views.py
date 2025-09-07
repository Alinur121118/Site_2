from django.shortcuts import render
from apps.users.models import InfoUser,Services,Experience,Education,Skills
# Create your views here.
def index(request):
    infouser = InfoUser.objects.latest("id")
    services = Services.objects.all()
    experience = Experience.objects.all().order_by("-id")
    education = Education.objects.all().order_by("-id")
    skills = Skills.objects.all()


    return render(request, "index.html", locals())