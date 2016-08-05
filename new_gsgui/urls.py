from django.conf.urls import patterns, include, url
from logger import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
admin.autodiscover()
router = DefaultRouter()
router.register(r'bmsdata', views.BMSViewSet)
router.register(r'mcdata', views.MCViewSet)
router.register(r'motordata', views.MotorViewSet)
router.register(r'generaldata', views.GeneralViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gsgui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Login, name='login'),
    url(r'^logout', views.Logout, name='logout'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
