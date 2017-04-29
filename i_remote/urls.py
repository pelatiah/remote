from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^remote_learning/professional/', views.training_professional, name='training_professional'),
    url(r'^remote_learning/student/', views.training_student, name='training_student'),
    url(r'^remote/design', views.remote_design, name='remote_design'),
    url(r'^remote/installation', views.remote_installation, name='remote_installation'),
    url(r'^profectional/training/form/$', views.form_professional_training, name='form_professional_training'),
    url(r'^student/training/form/$', views.form_student_training, name='form_student_training'),
    url(r'^thank_you/$', views.thank_you, name='thank_you'),
    url(r'^design/profectional/form$', views.form_design_prof, name='form_design_prof'),
    url(r'^design/self/form$', views.form_design_self, name='form_design_self'),
    url(r'^installation/form$', views.form_installation, name='form_installation'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]