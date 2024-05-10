from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from election_poll.views import *
urlpatterns = [
    path('',homepage, name='homepage'),
    path('elect_poll/',elect_poll, name='elect_poll'),
    path('el_login/',el_login, name='el_login'),
    path('el_signup/',el_signup, name='el_signup'),
    path('el_result/',elect_result, name='elect_result'),
    path('el_logout/', logout_el_User, name='logout_el_User'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('submit_vote/<str:party_name>/', submit_vote, name='submit_vote')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)