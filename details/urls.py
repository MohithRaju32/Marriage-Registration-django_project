
from django.urls import path
from .import views
from django.urls import include

urlpatterns = [
    path('registration_form', views.registration_form, name="registration_form"),
    path('final_page', views.final_page, name="final_page"),
    path('signout',views.signout,name="signout"),
]

urlpatterns += [
    path('edit_form', views.edit_form, name="edit_form"),
]