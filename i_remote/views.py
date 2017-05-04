from django.shortcuts import render, get_object_or_404, redirect
from .models import Design, DesignProfessional, TrainingStudent, DesignStudent,RemoteDesign, FormUse
from .models import RemoteInstallation, RemoteInstallationTwo, RemoteDesignTwo, DesignSelfComputer, DesignSelfComputerTwo
from django.utils import timezone
from .forms import FormProfessiona, FormStudent, FormDesignProf, FormDesignself, FormInstallation
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



def index(request):
    design = Design.objects.filter(publish_date__lte=timezone.now()).order_by('author')
    design_student = TrainingStudent.objects.filter(publish_date_student__lte=timezone.now()).order_by('title_student')
    remote_design = RemoteDesign.objects.filter(publish_date__lte=timezone.now()).order_by('title')
    remote_installation = RemoteInstallation.objects.filter(publish_date__lte=timezone.now()).order_by('title')
    return render(request, 'i_remote/index.html', {'design': design, 'design_student': design_student, 'remote_design': remote_design,
                                                   'remote_installation': remote_installation})


def training_student(request):
    design_student = TrainingStudent.objects.filter(publish_date_student__lte=timezone.now()).order_by('title_student')
    design_stud = DesignStudent.objects.filter(publish_date__lte=timezone.now()).order_by('title_stud')
    return render(request, 'i_remote/training_student.html', {'design_student': design_student, 'design_stud': design_stud})


def training_professional(request):
    detail = DesignProfessional.objects.all()
    return render(request, 'i_remote/training_professional.html', {'detail': detail})


def remote_design(request):
    remote_des = RemoteDesignTwo.objects.all()
    design_com = DesignSelfComputer.objects.all()
    return render(request, 'i_remote/remote_design.html', {'remote_des': remote_des, 'design_com': design_com})


def remote_installation(request):
    remote_install = RemoteInstallationTwo.objects.all()
    return render(request, 'i_remote/remote_installation.html', {'remote_install': remote_install})

def form_professional_training(request):
    form = FormProfessiona()
    return render(request, 'i_remote/form_professional_training.html', {'form': form})

def form_student_training(request):
    form = FormStudent()
    return render(request, 'i_remote/form_student_training.html', {'form': form})

def form_design_prof(request):
    form = FormDesignProf()
    return render(request, 'i_remote/form_design_prof.html', {'form': form})

def form_design_self(request):
    form = FormDesignself()
    return render(request, 'i_remote/form_design_self.html', {'form': form})

def form_installation(request):
    form = FormInstallation()
    return render(request, 'i_remote/form_installation.html', {'form': form})


def thank_you(request):
    return render(request, 'i_remote/thank_you.html', {})

def modification_page(request):
    return render(request, 'i_remote/modification_page.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



#def form_professional_training(request):
#    form = FormProfessiona()
 #   if request.method == "POST":
  #      form = FormProfessiona(request.POST)
   #     if form.is_valid():
    #        prof_training = form.save(commit=False)
     #       prof_training.detail = detail
      #      prof_training.save()
       #     return redirect('training_professional')
 #   else:
  #      form = FormUse()
   # return render(request, 'i_remote/form_professional_training.html', {'form': form})


# Create your views here.
