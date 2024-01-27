from django.contrib import admin
from django.urls import path
from . import views



app_name='web'




urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout,name='logout'),
    path('createpost/',views.createpost,name='createpost'),
    path('equipment_list/', views.equipment_list, name="equipments"),
    path('equipment_list/<str:category>', views.equipment_list, name="equipments"),
    path('finish_equipment/<int:id>',views.finish_equipment, name='finish_equipment'),
    path('change_status/<int:id>',views.change_status, name='change_status'),

]