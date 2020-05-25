from django.conf.urls import url
from . import views
from .views import FORMS


urlpatterns = [
    url(r'^$', views.calculator, name='calculator'),
    url(r'^remove/(?P<id>\w+)/(?P<element_id>\d+)/$', views.calculator_remove, name='calculator_remove'),
    url(r'^addstudent/$', views.AddStudentWizard.as_view(FORMS), name='addstudent'),
    url(r'^test/$',views.test),
    url(r'^add/$', views.HomePage.as_view()),


]
app_name = 'calculator'