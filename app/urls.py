from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register_user,name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    path('business/',views.business,name='business'),
    path('add_a_business/',views.add_a_business,name='add_a_business'),
    path('neighborhood/',views.neighborhood,name='neighborhood'),
    path('add_a_neighborhood/',views.add_a_neighborhood,name='add_a_neighborhood'),
    path('post/',views.posts,name='posts'),
    path('post/<int:id>/',views.posts,name='post'),
    path('add_a_post/',views.add_a_post,name='add_a_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   