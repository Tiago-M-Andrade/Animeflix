"""
URL configuration for animeflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, reverse_lazy
from .views import HomePage, HomeAnimes, AnimeDetail, SearchAnime, PlayAnime, ProfileEdit, CreateAccount
from django.contrib.auth import views as auth_view

app_name = 'anime'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('animes/', HomeAnimes.as_view(), name='animes'),
    path('animes/<int:pk>', AnimeDetail.as_view(), name='details'),
    path('animes/<int:pk>/play/<int:pk2>', PlayAnime.as_view(), name='play'),
    path('animes/search', SearchAnime.as_view(), name = 'search'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name ='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name ='logout'),
    path('profile/edit/<int:pk>', ProfileEdit.as_view(), name = 'profileedit'),
    path('profile/edit/password/', auth_view.PasswordChangeView.as_view(template_name='changepass.html', 
                                                                        success_url=reverse_lazy('anime:animes')), name = 'changepass'),
    path('profile/create/', CreateAccount.as_view(), name = 'createaccount'),
]