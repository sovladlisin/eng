from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    path('mail', views.Email, name='mail'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^user_login/$', views.user_login, name='user_login'),
    path('home', views.Home, name='home'),
    path('jobs', views.Jobs, name='jobs'),
    path('requests', views.Requests, name='requests'),
    path('info', views.Info, name='info'),
    path('portfolio', views.PortfolioView, name='portfolio'),
    path('certificates', views.CertificatesView, name='certificates'),
    path('contacts', views.ContactsView, name='contacts'),
    url(r'^job/(?P<pk>\d+)/edit/$', views.JobEdit, name='jobEdit'),
    url(r'^job/(?P<pk>\d+)/description/$', views.JobView, name='jobView'),
    url(r'^portfolio/(?P<pk>\d+)/jobDescription/$',
        views.PortfolioJobView, name='portfolioJobView'),

    url(r'^request/(?P<pk>\d+)/delete/$',
        views.DeleteRequest, name='deleteRequest'),
]
