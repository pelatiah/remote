from django.contrib import admin
from .models import Design, DesignProfessional, TrainingStudent, DesignStudent, RemoteDesign, FormUse
from .models import RemoteInstallation, RemoteInstallationTwo, RemoteDesignTwo, DesignSelfComputer, DesignSelfComputerTwo

admin.site.register(Design)
admin.site.register(DesignProfessional)
admin.site.register(TrainingStudent)
admin.site.register(DesignStudent)
admin.site.register(RemoteDesign)
admin.site.register(RemoteDesignTwo)
admin.site.register(RemoteInstallation)
admin.site.register(RemoteInstallationTwo)
admin.site.register(DesignSelfComputer)
admin.site.register(DesignSelfComputerTwo)
admin.site.register(FormUse)
# Register your models here.
