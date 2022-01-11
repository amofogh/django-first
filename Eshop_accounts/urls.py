from django.urls import path
from .views import login_user, register_user, log_out, user_panel, edit_profile

app_name = 'accounts'

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register_user, name='register'),
    path('logout', log_out),
    path('panel', user_panel, name='user_panel'),
    path('panel/edit', edit_profile, name='edit_profile'),

]
