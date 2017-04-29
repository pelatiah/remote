from django.db import models
from django.utils import timezone

class Design(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    preview = models.TextField()
    publish_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class TrainingStudent(models.Model):
    author_student = models.ForeignKey('auth.User')
    title_student = models.CharField(max_length=200)
    preview_student = models.TextField()
    publish_date_student = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publish_date_student = timezone.now()
        self.save()

    def __str__(self):
        return self.title_student

class RemoteDesign(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    preview = models.TextField()
    publish_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class RemoteInstallation(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    preview = models.TextField()
    publish_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class DesignSelfComputer(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    preview = models.TextField()
    publish_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title







class DesignProfessional(models.Model):
    prof = models.ForeignKey('i_remote.Design', related_name='designprofessional')
    title_prof = models.CharField(max_length=200)
    detail_specification = models.TextField()
    publish_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.detail_specification

class DesignStudent(models.Model):
    stud = models.ForeignKey('i_remote.TrainingStudent', related_name='designstudent')
    title_stud = models.CharField(max_length=200)
    detail_specification = models.TextField()
    publish_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.detail_specification

class RemoteDesignTwo(models.Model):
    remote = models.ForeignKey('i_remote.RemoteDesign', related_name='remotedesign')
    title_remote = models.CharField(max_length=200)
    detail_specification = models.TextField()
    publish_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.detail_specification

class RemoteInstallationTwo(models.Model):
    install = models.ForeignKey('i_remote.RemoteInstallation', related_name='remoteinstallation')
    title_install = models.CharField(max_length=200)
    detail_specification = models.TextField()
    publish_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.detail_specification

class DesignSelfComputerTwo(models.Model):
    design_self = models.ForeignKey('i_remote.DesignSelfComputer', related_name='designselfcomputer')
    title_self_com = models.CharField(max_length=200)
    preview = models.TextField()
    publish_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




SOFTWARE_LIST = (
    ('ACAD', 'AutoCAD'),
    ('INVENTOR', 'Autodesk inventor'),
    ('MEP', 'Revit MEP'),
    ('ARCHITECTURE', 'Revit  Architecture'),
    ('STRUCTURE', 'Revit Structure'),
    ('MAX', '3ds Max'),
)

DETAIL_SPECIFICATION = (
    ('CALL', 'Calls'),
    ('EMAIL', 'Emails'),
    ('SKYPE', 'Skype Calls'),
    ('CHAT', 'Chats'),
    ('VIEWER', 'Team Viewer'),
)

LICENSE = (
    ('NON TRY', 'Licensed'),
    ('TRY', 'Trial'),
)

OUTPUT = (
    ('NATIVE', 'Native File'),
    ('DWF', 'DWF Format'),
    ('PDF', 'PDF Format'),
)

TYPE = (
    ('ALONE', 'Stand Alone Installation'),
    ('NETWORK', 'Network Installation'),
)

REQUIREMENT = (
    ('YES', 'Yes up to system requirement'),
    ('NO', 'No need to be upgraded'),
    ('NONO', 'No I want to use it like that')
)

class FormUse(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    software = models.CharField(max_length=3, choices=SOFTWARE_LIST)
    training_duration_in_weeks = models.CharField(max_length=2)
    number_of_trainee = models.CharField(max_length=2)
    school_name = models.CharField(max_length=200)
    detail_and_specification = models.CharField(max_length=3, choices=DETAIL_SPECIFICATION)
    license_type = models.CharField(max_length=3, choices=LICENSE)
    prefered_output = models.CharField(max_length=3, choices=OUTPUT)
    installation_type = models.CharField(max_length=3, choices=TYPE)
    system_requirement = models.CharField(max_length=3, choices=REQUIREMENT)
    created_date = models.DateTimeField(default=timezone.now)
    approved_form = models.BooleanField(default=True)


    def approve(self):
        self.approved_form = True
        self.save()

    def __str__(self):
        return self.title
