from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render
from django.conf import settings
from django.views.static import serve
from complaints.models import Announcement


def home_view(request):
    announcements = Announcement.objects.filter(is_active=True).order_by('-date_posted')[:6]
    return render(request, 'home.html', {'announcements': announcements})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('lost-and-found/', include('lost_and_found.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('complaints/', include('complaints.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
