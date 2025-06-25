
from django.contrib import admin
from django.urls import path
from users_auth.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_page,name='login'),
    path('signup_page',signup_page,name='signup'),
    path('home',home_page,name='home'),
    path('logout',logout_page,name='logout'),
    path('edit_profile/<int:id>',edit_profile,name='edit_profile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
