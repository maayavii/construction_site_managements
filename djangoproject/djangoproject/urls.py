"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from djangoapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('product/',views.product,name='product'),
    path('contact/',views.contact,name='contact'),
    path('addProduct/',views.addProduct,name='addProduct'),
    path('store/',views.store,name='store'),
    path('store/',views.store,name='store'),
    path('error/',views.error,name='error'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('edit/<int:pk>/', views.editProduct, name='editProduct'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('accounts/', views.accounts_view, name='accounts'),
 path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts.html'), name='login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
 
   
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
