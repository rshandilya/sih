from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('sign-up',views.sign_up, name='sign-up'),
    path('profile',views.profile, name='profile'),
    path('profile/<int:id>/edit',views.edit_profile, name='edit_profile'),
    path('profile/medicine-donations',views.donation_list, name='donations'),
]