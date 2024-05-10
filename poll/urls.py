
from django.urls import path
from poll import views as poll_views

urlpatterns = [
    
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('login/', poll_views.login_page, name='login'),
    path('signup/', poll_views.signup_page, name='signup'),
    path('logout/', poll_views.logoutUser, name='logoutUser'),

    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
]