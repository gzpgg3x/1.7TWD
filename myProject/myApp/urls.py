from django.conf.urls import patterns, include, url
# from django.contrib import admin
from myApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"), 
    # url(r'^/category/?P<slug>$/', views.category, name="category"),  
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name="category"), 
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),  # New!   
)
