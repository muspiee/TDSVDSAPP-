from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import *
from Accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aboutus/', about, name='aboutus'),
    path('mission/', mission, name='mission'),
    path('users/', users, name='users'),
    path('use/', use, name='use'),
    path('renew-account/', renew_account, name='renew_account'),
    path('deactivate_user/', deactivate_user, name='deactivate_user'),
    path('contact/', contact, name='contact'),
    path('whattodo/', whattodo, name='what'),
    path('how/', how, name='how'),
    path('active/', activation_view, name='active'),
    path('otp/', otp_verify, name='otp'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('get-suggestions/', get_spelling_suggestions, name='get_spelling_suggestions'),
    path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
