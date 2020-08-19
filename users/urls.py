from django.urls import path
from .views import profile, teachRequest, AccountInfo

app_name = 'users'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('teacher/', teachRequest, name='teacher'),
    path('account_info/', AccountInfo.as_view(), name='account-info')
    
]
