from django.urls import path

from . import views

app_name = 'register'
urlpatterns = [

	# ex: /register/
    #path('', views.HomeView, name='home'),
	# ex: /register/login/
    #path('login/', views.LoginView.as_view(), name='login'),
    # ex: /register/logout/
    #path('logout/', views.LogoutView.as_view(), name='logout'),
    # ex: /register/signup/
    path('signup/', views.SignUpView.as_view(), name='signup'),

]