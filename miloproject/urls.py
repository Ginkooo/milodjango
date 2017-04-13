"""miloproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from foobar import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list/$', views.list_users),
    url(r'^list/(csv)/$', views.list_users),
    url(r'^view/([0-9]+)/$', views.view_user),
    url(r'^add/$', views.add_user),
    url(r'^edit/([0-9]+)/$', views.edit_user),
    url(r'^$', views.list_users, name='home'),
]
