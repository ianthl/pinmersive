"""pinmersive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from users import views as users_views
from pins import views as pins_views

from users.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pin/', include('pins.urls', namespace="pins")),
    url(r'^categories/', include('categories.urls', namespace="categories")),

    url(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', users_views.register, name='register'),
    url(r'^settings/$', users_views.settings, name='settings'),

    url(r'^search/pins/$', pins_views.search, name='search'),

    url(r'^(?P<username>\w+)/', include('users.urls', namespace="users")),
    url(r'^$', users_views.feed, name='home'),
]

if settings.DEBUG:
    # Static and Media ulrs
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # django-debug-toolbar urls
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns