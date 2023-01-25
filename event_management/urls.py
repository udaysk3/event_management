
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from .views import dashboard, login_page, logut_page,dashboard2,register
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('dashboard2', dashboard2, name="dashboard2"),
    path('login/', login_page, name='login'),
    path('logout/', logut_page, name='logout'),
    path("register/", register, name="register"),   
    path('events/', include('events.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)